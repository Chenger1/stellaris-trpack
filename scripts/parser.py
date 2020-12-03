"""
                              ↓ Инициализация данных ↓
"""

from re import compile
from shutil import copyfile

from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files, \
    replace_last_line_symbol, check_new_line_sym_ending

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


def separate_unnecessary_parts(prepared_line, file_type):
    unnecessary_parts = {
        'localisation': ['\"', '§L', '§!', ],
        'name_lists': ['\"', ]
    }
    unnecessary_parts = unnecessary_parts[file_type]
    index = 0
    prepared_line = [prepared_line, ]

    for part in prepared_line:
        if ' +' in part:
            index = unnecessary_parts.index(part[part.index(" +") + 2:])

        while index < len(unnecessary_parts):
            symbol = unnecessary_parts[index]

            if symbol in part:
                symbol_pos = part.find(symbol)
                prepared_line.append(part[symbol_pos + (len(symbol)):])
                prepared_line[-2] = (part[:symbol_pos - 1]) + f" +{symbol}"
            index += 1
        else:
            index = 0

    return prepared_line


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

                prepared_line = separate_unnecessary_parts(prepared_line, file_type)
                for part in prepared_line:
                    part = check_new_line_sym_ending(part)
                    source_text.append(part)
                    source.write(part)
            else:
                source_text.append('\n')
                source.write('\n')
    source_text = replace_last_line_symbol(original_text, source_text, source_file_path)

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

    prepare_temp_files(original_text, source_text)
