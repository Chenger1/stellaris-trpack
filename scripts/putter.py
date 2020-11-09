# TODO Рассмотреть возможности упростить алгоритм
# TODO Добавить поинтер, читать исходный файл, resource и пользовательский вариант перевода
# начиная с первой строки, брать строку из оригинального файла,
# заменять в ней строку из resource строкой из пользовательского перевода и увеличивать поинтер на 1,
# снова
# в конце списка записывать этот массив строк в локализированный файл
"""
                              ↓ Инициализация данных ↓
"""

import re
from os import path, mkdir
from itertools import islice

from scripts.utils import paradox_folder


"""
                              ↓ Работа с файлом локализации ↓
"""


def search(file_type, line):
    subs = {
            'localisation': re.compile(': |:0|:1|:"'),
            'name_lists': re.compile('"|'),
            'species_names': re.compile('[#{}]')
            }

    match = subs[file_type].search(line)
    if match is not None:
        return 1
    else:
        return 0


def put_lines(file):
    trlist = []
    nonlist = []

    new_file_name = file.original_file_name.replace("english", file.target_language)
    new_file_path = file.original_file_path.split(f'{file.mod_id}\\')[-1].split(f'\\{file.original_file_name.split(".")[0]}')[0]

    # for folder in new_file_path.split('\\'):

    new_file = f'{paradox_folder}\\mod\\local_localisation\\{new_file_path}\\{new_file_name}'
    new_file = open(f"{new_file}", 'w', encoding='utf-8')

    l_english = open(file.original_file_path, 'r', encoding='utf-8')
    user_input = open(file.user_input_file_path, 'r', encoding='utf-8')
    # TODO Создавать нужную директорию перед сохранением файла
    #  _file = open(f"{new_file}", 'w', encoding='utf-8')
    # FileNotFoundError: [Errno 2] No such file or directory:
    # 'C:\\Users\\Letiso\\Documents\\Paradox Interactive\\Stellaris\\mod\\local_localisation\\localisation\\###english###\\geth_l_russian.yml'

    new_file.write('\ufeff')

    for line in user_input:
        trlist.append(line.rstrip())

    if file.type in 'localisation':
        new_file.write(f'l_{file.target_language}:\n')

    for index, line in enumerate(islice(l_english, 1, None)):
        nonlist.append(line.rstrip())
        if (search(subs[file.type], line) == 1) and ((line[0] and line[1]) != '#'):
            a = line.find('"')
            curstr = line[0:a + 1] + trlist[index + 1] + '"'
        else:
            curstr = nonlist[index]
        new_file.write(curstr + '\n')

    l_english.close()
    user_input.close()
    new_file.close()
