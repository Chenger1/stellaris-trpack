"""
                              ↓ Инициализация данных ↓
"""

from os import path, mkdir

from scripts.utils import local_mod_path
from copy import copy

"""
                              ↓ Сохранение завершенной локализации ↓
"""


def put_lines(file):
    localisation_path_list = file.original_file_path.split(f'{file.mod_id}\\')[-1].split('\\')[0:-2]
    localisation_name = file.original_file_name.replace("english", file.target_language)
    localisation_path = f'{local_mod_path}'
    index = 0

    for folder in localisation_path_list:
        localisation_path += f'\\{folder}'
        if path.isdir(localisation_path) is False:
            mkdir(localisation_path)
    localisation_path += f'\\{localisation_name}'

    with open(file.original_file_path, 'r', encoding='utf-8') as original, \
            open(file.source_file_path, 'r', encoding='utf-8') as source, \
            open(file.user_input_file_path, 'r', encoding='utf-8') as user_input:
        original = original.readlines()
        source = source.readlines()
        user_input = user_input.readlines()

    with open(f"{localisation_path}", 'w', encoding='utf-8') as localisation:
        if file.type in 'localisation':
            original[0] = original[0].replace('l_english', f'l_{file.target_language}')
        localisation.write('\ufeff')

        for line in original:
            if ' +' in source[index]:
                while ' +' in source[index]:
                    line = line.replace(source[index][:-3], user_input[index][:-3])
                    index += 1
            else:
                line = line.replace(source[index][:-1], user_input[index][:-1])
                index += 1
            localisation.write(line)


"""
                              ↓ Обновление файла ↓
"""


def update_lines(main_file_path, new_file_path):
    updated_file_path = main_file_path.replace('.yml', '_updated.yml')
    file_type = 'localisation' if '.yml' in updated_file_path else '.txt'

    with open(main_file_path, 'r', encoding='utf-8') as main_text, \
            open(new_file_path, 'r', encoding='utf-8') as new_text:
        main_text = main_text.readlines()
        new_text = new_text.readlines()
        updated_text = copy(new_text)

    if file_type == 'localisation':
        new_text_vars = [new_line.split('"')[0] for new_line in new_text]
        main_text_vars = [main_line.split('"')[0] for main_line in main_text]
        index_dict = {index: None for index, var in enumerate(new_text_vars)}
        # TODO требуется добавить поддержку нейм-листов ↓

    for index in index_dict:
         if new_text_vars[index] in main_text_vars:
            index_dict[index] = main_text_vars.index(new_text_vars[index])

    for new_index, main_index in index_dict.items():
        if main_index is not None:
            updated_text[new_index] = main_text[main_index]

    with open(f"{updated_file_path}", 'w', encoding='utf-8') as updated:
        updated.write(''.join(updated_text))
