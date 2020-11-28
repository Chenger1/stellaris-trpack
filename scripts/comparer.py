"""
                              ↓ Инициализация данных ↓
"""

from os import path, mkdir

from scripts.utils import local_mod_path


"""
                              ↓ Сохранение завершенной локализации ↓
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

        # TODO сделать сборку строки используя ['...', '... +', '...']
        for line in original:
            line = line.replace(source[pointer], user_input[pointer])
            localisation.write(line)
            pointer += 1


"""
                              ↓ Обновление файла ↓
"""


def update_lines(main_file_path, new_file_path):
    pointer = 0
    compared_file_path = main_file_path.replace('.yml', '_updated.yml')
    updated_text = []
    file_type = 'localisation' if '.yml' in compared_file_path else '.txt'

    with open(f"{compared_file_path}", 'w', encoding='utf-8') as updated, \
            open(main_file_path, 'r', encoding='utf-8') as main_text, \
            open(new_file_path, 'r', encoding='utf-8') as new_text:
        main_text = main_text.readlines()
        new_text = new_text.readlines()
        updated.write('\ufeff')

        # TODO требуется дальнейшая работа ↓
        for new_line in new_text:
            try:
                main_line = main_text[pointer]
            except IndexError:
                main_line = main_text[len(main_text) - 1]
            new_line_check = new_line.split('"')[0] if file_type == 'localisation' else ''
            main_line_check = main_line.split('"')[0] if file_type == 'localisation' else ''

            if main_line_check == new_line_check:
                updated_text.append(main_line)
                pointer += 1
            elif [new_line for new_line in new_text if main_line_check in new_line]:
                updated_text.append(new_line)
            else:
                pointer += 1
                updated_text.append(new_line)

        updated.write(''.join(updated_text))
