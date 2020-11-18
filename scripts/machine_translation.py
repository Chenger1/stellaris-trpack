"""
                              ↓ Инициализация данных ↓
"""

from re import compile

from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory


"""
                              ↓ Перевод временных файлов ↓
"""
# TODO rework


def search(subs, line):
    counter = 0
    for i in range(len(subs)):
        if subs[i] in line:
            counter += 1
    if counter != 0:
        return 1
    else:
        return 0


def slice_string(line: str, specials={'§', '$', '£'}):
    result = []
    if '[' in line:
        pattern = compile(r'\[.*?]')
    elif set(line) & specials:
        pattern = compile(r'[§$£].*?[§$£]')
    else:
        result.append(line)
        return result
    result = pattern.split(line)
    return result


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

    def wrapper(line, tr_language, translator):
        ru_line = func(line, tr_language, translator)
        for sym in symbols:
            ru_line = ru_line.replace(sym, symbols[sym])
        return ru_line

    return wrapper


@replacing_invalid_new_line_symbol
def translating_line(line: str, tr_language, translator=None) -> str:
    while True:
        try:
            translation = translator.translate(line, dest=tr_language)
        except AttributeError:
            continue
        else:
            return translation.text


def line_processing(line: str, translator, tr_language) -> str:
    temp = slice_string(line)
    translated = list(map(lambda x: translating_line(x, tr_language, translator), temp))
    for en, ru in zip(temp, translated):
        line = line.replace(en[:-1], ru)
    return line


def defining_translator(func):
    translator = Translator()

    def wrapper(line):
        tr_line = func(line, translator)
        return tr_line

    return wrapper


@defining_translator
def translate_line(line, translator=None):
    DetectorFactory.seed = 0

    # TODO It's unnecessary to get target language every time
    with open("Properties.json", 'r', encoding='utf-8') as properties:
        properties = load(properties)

        if len(line) > 2:
            test = detect(line)
            if test != properties["target_language"]:
                translation = line_processing(line, translator, properties["target_language"])
            else:
                translation = line
        else:
            translation = line
        return translation
