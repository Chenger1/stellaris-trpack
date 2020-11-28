"""
                              ↓ Инициализация данных ↓
"""

from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory


"""
                              ↓ Перевод временных файлов ↓
"""


def replacing_invalid_new_line_symbol(func):
    symbols = {
        '\ N \ n': '\\n\\n',
        '\ n \ n': '\\n\\n',
        '\ n': '\\n',
        '\ N': '\\n',
        '\ П': '\\n',
        '! \\n': '!\\n',
        '. \\n': '.\\n',
    }

    def wrapper(line, target_language, translator):
        ru_line = func(line, target_language, translator)
        for sym in symbols:
            ru_line = ru_line.replace(sym, symbols[sym])
        return ru_line

    return wrapper


@replacing_invalid_new_line_symbol
def translating_line(line: str, target_language, translator=None) -> str:
    while True:
        try:
            translation = translator.translate(line, dest=target_language)
        except AttributeError:
            continue
        else:
            return translation.text


def defining_translator(func):
    translator = Translator()
    with open("Properties.json", 'r', encoding='utf-8') as properties:
        target_language = load(properties)["target_language"]

    def wrapper(line):
        tr_line = func(line, translator, target_language)
        return tr_line

    return wrapper


@defining_translator
def translate_line(line, translator=None, target_language=None):
    DetectorFactory.seed = 0
    test = detect(line)

    # TODO Добавить разбор строки, используя ['...', '... +', '...']  ↓

    if test != target_language:
        translation = translating_line(line, target_language, translator)
    else:
        translation = line

    return translation
