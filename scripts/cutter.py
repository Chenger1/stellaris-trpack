"""
                              ↓ Инициализация данных ↓
"""

import re

from scripts.translator import translate_line
from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files
from shutil import copyfile

"""
                                ↓ Парсинг файлов с расширением .yml ↓
"""


def loc_search(subs, line):
    match = subs.search(line)
    if match is not None:
        return 1
    else:
        return 0


def cutting_loc_lines(source_file_path, original_file_path):
    subs = re.compile(': |:0|:1|:"]')

    orig_text = []
    with open(original_file_path, 'r', encoding='utf-8') as localisation_file:
        with open(source_file_path, 'w', encoding='utf-8') as cutter_file:
            for line in localisation_file:
                if loc_search(subs, line) == 1:
                    if (line[0] and line[1]) != '#':
                        a = line.find('"')
                        lt = line[a + 1:-2]
                        orig_text.append(lt + '\n')
                        cutter_file.write(lt + '\n')
                    else:
                        orig_text.append('\n')
                        cutter_file.write('\n')
                else:
                    orig_text.append('\n')
                    cutter_file.write('\n')

    return orig_text


"""
                                ↓ Парсинг файлов с расширением .txt ↓
"""


def name_search(subs, line):
    match = subs.search(line)
    if match is None:
        return 1
    else:
        return 0


def cutting_name_list_lines(source_file_path, original_file_path):
    subs = re.compile('[#{}]')

    orig_text = []
    with open(original_file_path, 'r', encoding='utf-8') as name_list_file:
        with open(source_file_path, 'w', encoding='utf-8') as cutter_file:
            for line in name_list_file:
                if name_search(subs, line) == 1 and line[0] != '\n':
                    if '=' in line and '"' in line:
                        a = line.find('"')
                        lt = line[a + 1:-2].replace('%O%', '-th')
                        orig_text.append(lt + '\n')
                        cutter_file.write(lt + '\n')
                    elif '=' not in line and '\t' not in line[-2]:
                        lt = line.replace('\t', '').replace('    ', '')
                        orig_text.append(lt)
                        cutter_file.write(lt)
                    else:
                        orig_text.append('\n')
                        cutter_file.write('\n')
                else:
                    orig_text.append('\n')
                    cutter_file.write('\n')

    return orig_text


"""
                                ↓ Создание временных файлов ↓
"""


def cutter_main(mod_path, mod_id, file_path):
    orig_text = []
    machine_text = []
    temp_folder = create_temp_folder(mod_id, file_path)
    write_data_about_file(temp_folder, file_path)
    copyfile(f'{mod_path}\\{file_path}', data["original_file_path"])

    if '.yml' in data["original_file_name"]:
        orig_text = cutting_loc_lines(data["source_file_path"], data["original_file_path"])
    elif '.txt' in data["original_file_name"]:
        orig_text = cutting_name_list_lines(data["source_file_path"], data["original_file_path"])

    for line in orig_text:
        machine_text.append(translate_line(line))
    prepare_temp_files(machine_text)
