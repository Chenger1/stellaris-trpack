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
    translation = translator.translate(line, src='en', dest=target_language)

    return translation.text


def defining_translator(func):
    translator = Translator(service_urls=['translate.googleapis.com',
                                          'translate.google.com'])
    with open("Properties.json", 'r', encoding='utf-8') as properties:
        target_language = load(properties)["target_language"]

    def wrapper(line, file_type):
        translation = func(line, file_type, target_language, translator)

        return translation

    return wrapper


@defining_translator
def translate_line(line, file_type, target_language=None, translator=None):
    DetectorFactory.seed = 0

    if detect(line) != target_language:
        translation = translating_line(line, target_language, translator)
    else:
        translation = line

    if type(translation) is not str:
        raise ConnectionError

    return translation if file_type == 'localisation' \
        else translation.title()
