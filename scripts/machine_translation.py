"""
                              ↓ Инициализация данных ↓
"""

from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory


"""
                              ↓ Перевод временных файлов ↓
"""


def translating_line(line: str, target_language, translator=None) -> str:
    translation = translator.translate(line, dest=target_language)

    return translation.text


def defining_translator(func):
    translator = Translator(service_urls=['translate.googleapis.com'])
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

    if test != target_language:
        translation = translating_line(line, target_language, translator)
    else:
        translation = line

    return translation
