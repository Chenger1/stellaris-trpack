"""
                              ↓ Инициализация данных ↓
"""

from re import compile, finditer, findall
from shutil import copyfile
from copy import copy

from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files, check_new_line_sym_ending

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


def symbols_init(func):
    symbols_dict = {
            'localisation': ['\"', '§L', '§!', '\\\\n'],
            'name_lists': ['\"', ' ']
            }

    def wrapper(prepared_line, file_type):
        symbols = symbols_dict[file_type]
        separated_parts = func(prepared_line, file_type, symbols)

        if ' +' in separated_parts[-1]:
            separated_parts[-1] = separated_parts[-1].replace(' +', '')

        return separated_parts

    return wrapper

@symbols_init
def separate_unnecessary_parts(prepared_line, file_type, symbols):
    symbol_index_list, separated_parts, prev_index, prev_symbol  = [], [prepared_line, ], 0, ''

    for symbol in symbols:
        index_list = [(index.start(), symbol) for index in finditer(symbol, prepared_line)
                              if type(index.start()) is int]
        temp_index_list = copy(index_list)

        if file_type == 'name_lists' and symbol_index_list and symbol == ' ':
            count = 1
            quote_start_index, quote_end_index = symbol_index_list[count - 1], symbol_index_list[count]

            for space_index in index_list:
                if space_index[0] >= quote_end_index[0] and quote_end_index[0] != symbol_index_list[-1][0]:
                    count += 1
                else:
                    temp_index_list.remove(space_index)

        symbol_index_list += temp_index_list
    symbol_index_list.sort()

    for index, symbol in symbol_index_list:
        append_list = [prepared_line[prev_index + len(prev_symbol):index],
                       prepared_line[index + (len(symbol) if symbol != '\\\\n' else + 2):]]
        append_list = [part for part in append_list
                       if part != '' and part != '\n' and part != ' ']
        if append_list:
            for part_index, part in enumerate(append_list):
                if part_index == 0:
                    if len(append_list) > 1:
                        separated_parts[-1] = f'{part} +'
                    else:
                        separated_parts[-1] = part
                else:
                    separated_parts.append(part)
        else:
            separated_parts.pop()

        prev_index, prev_symbol = index, symbol

    return separated_parts


def strings_parsing(source_file_path, original_file_path, file_type):
    source_text = []
    with open(original_file_path, 'r', encoding='utf-8') as original_text,\
            open(source_file_path, 'w', encoding='utf-8') as source:
        original_text = original_text.readlines()
        for line in original_text:
            if search_for_nesessary(file_type, line) and search_for_unnesessary(file_type, line):
                symbol = '\t' if '\t' in line else line.find('"')

                if type(symbol) is not int:
                    prepared_line = line.split(symbol)[-1]

                    if prepared_line[0].islower():
                        # Если первая буква строки не является заглавной,
                        # то есть перед необходимым текстом имеются ненужные элементы

                        quote_symbol = line.find('\"') - 1
                        # Если в строке есть '"',
                        # то делаем срез от начала кавычки до конца строки

                        letter_symbol = line.find('=') + 2
                        # Если в строке нет кавычки, но есть '=',
                        # если первая буква после '=' является заглавной,
                        # то делаем срез от начала первой буквы до конца строки

                        prepared_line = line[quote_symbol:] if '\"' in line \
                            else line[letter_symbol if line[letter_symbol].isupper()
                                      else -1:]
                        # В противном случае оставляем только '\n'
                else:
                    prepared_line = line[symbol:]

                if '_' not in prepared_line:
                    for part in separate_unnecessary_parts(prepared_line, file_type):
                        part = check_new_line_sym_ending(part)
                        source_text.append(part)
                else:
                    source_text.append('\n')
            else:
                source_text.append('\n')

    return original_text, source_text


"""
                                ↓ Создание временных файлов ↓
"""


def parser_main(mod_path, mod_id, file_path):
    temp_folder = create_temp_folder(mod_id, file_path)
    write_data_about_file(temp_folder, file_path)
    copyfile(f'{mod_path}\\{file_path}', data["original_file_path"])

    if '.yml' in data["original_file_name"]:
        file_type = 'localisation'
    else:
        file_type = 'name_lists'
    original_text, source_text = strings_parsing(data["source_file_path"], data["original_file_path"], file_type)

    prepare_temp_files(original_text, source_text, file_type, None)
