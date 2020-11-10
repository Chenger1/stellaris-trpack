"""
                              ↓ Инициализация данных ↓
"""

from os import path, mkdir

from scripts.utils import local_mod_path

"""
                              ↓ Создание переведенного файла локализации ↓
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
