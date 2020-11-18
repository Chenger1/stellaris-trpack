"""
                              ↓ Инициализация данных ↓
"""

from re import compile
from shutil import copyfile

from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files, remove_extra_new_line_symbols

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

    # for line in source_text:
    #     machine_text.append(translate_line(line))
    prepare_temp_files(machine_text)

