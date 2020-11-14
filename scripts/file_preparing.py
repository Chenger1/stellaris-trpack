"""
                              ↓ Инициализация данных ↓
"""

from re import compile
from os import path, mkdir
from shutil import copyfile

from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory

from scripts.utils import local_mod_path, write_data_about_file, create_temp_folder, data, \
    prepare_temp_files, remove_extra_new_line_symbols


"""
                              ↓ Парсинг файлов ↓
"""


def search_for_nesessary(file_type, line):
    subs = {
        'localisation': compile(': |:0|:1|:"'),
        'name_lists': compile('\t\t|\t"|= ')
    }

    if subs[file_type].search(line) is not None:
        return True
    else:
        return False


def search_for_unnesessary(file_type, line):
    subs = {
        'localisation': compile('#'),
        'name_lists': compile('[#{}]')
    }

    if subs[file_type].search(line) is None:
        return True
    else:
        return False


# TODO Добавить в обработку исключений закрывающие символы и связки символов по типу
#  symbol = [§!, ..., §L]
#  через replace(symbol, '')
"""
    §L
        This species is made up of the executive terminals of a single Machine Intelligence, originally built by Quarians.
    §!
    \n
"""


def strings_parsing(source_file_path, original_file_path, file_type):
    source_text = []
    with open(original_file_path, 'r', encoding='utf-8') as original_text:
        original_text = original_text.readlines()
    with open(source_file_path, 'w', encoding='utf-8') as source:
        for line in original_text:
            if search_for_nesessary(file_type, line) and search_for_unnesessary(file_type, line):
                symbol = '\t' if '\t' in line else line.find('"')

                if type(symbol) is not int:
                    prepared_line = line.split(symbol)[-1]

                    if prepared_line[0].islower():
                        # Если первая буква строки не является заглавной

                        quote_symbol = line.find('\"') - 1
                        # Если в строке есть '"',
                        # то делаем срез от начала кавычки до конца строки

                        letter_symbol = line.find('=') + 2
                        # Если в строке нет кавычки, но есть '=',
                        # если первая буква после '=' является заглавной,
                        # то делаем срез от начала первой буквы до конца строки

                        prepared_line = line[quote_symbol:] if '\"' in line \
                        else line[letter_symbol if line[letter_symbol].isupper()
                                  else len(line) - 1:]
                        # В противном случае оставляем только '\n'
                else:
                    prepared_line = line[symbol + 1: - 2]
                source_text.append(f'{prepared_line}')
                source.write(f'{prepared_line}')
            else:
                source_text.append('\n')
                source.write('\n')
    source_text = remove_extra_new_line_symbols(source_text, source_file_path)

    return source_text


"""
                                ↓ Создание временных файлов ↓
"""


def parser_main(mod_path, mod_id, file_path):
    file_type = None
    machine_text = []

    temp_folder = create_temp_folder(mod_id, file_path)
    write_data_about_file(temp_folder, file_path)
    copyfile(f'{mod_path}\\{file_path}', data["original_file_path"])

    if '.yml' in data["original_file_name"]:
        file_type = 'localisation'
    elif '.txt' in data["original_file_name"]:
        file_type = 'name_lists'
    source_text = strings_parsing(data["source_file_path"], data["original_file_path"], file_type)

    for line in source_text:
        machine_text.append(translate_line(line))
    prepare_temp_files(machine_text)


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


"""
                              ↓ Компоновка файлов ↓
"""
# TODO Create

"""
                              ↓ Сохранение готовой локализации ↓
"""


def put_lines(file):
    pointer = 0
    localisation_path_list = file.original_file_path.split(f'{file.mod_id}\\')[-1].split('\\')[0:-2]
    localisation_name = file.original_file_name.replace("english", file.target_language)
    localisation_path = f'{local_mod_path}'

    for folder in localisation_path_list:
        localisation_path += f'\\{folder}'
        if path.isdir(localisation_path) is False:
            mkdir(localisation_path)
    localisation_path += f'\\{localisation_name}'

    with open(f"{localisation_path}", 'w', encoding='utf-8') as localisation, \
            open(file.original_file_path, 'r', encoding='utf-8') as original, \
            open(file.source_file_path, 'r', encoding='utf-8') as source, \
            open(file.user_input_file_path, 'r', encoding='utf-8') as user_input:
        original = original.readlines()
        source = source.readlines()
        user_input = user_input.readlines()
        localisation.write('\ufeff')

        if file.type in 'localisation':
            original[0] = original[0].replace('l_english', f'l_{file.target_language}')
        for line in original:
            line = line.replace(source[pointer], user_input[pointer])
            localisation.write(line)
            pointer += 1
