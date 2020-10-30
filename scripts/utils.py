"""
                                ↓ Инициализация основных файлов и данных ↓
"""

import json
import os
import win32api
import zipfile
import shutil

from locale import getdefaultlocale
from googletrans.constants import LANGUAGES

from scripts.collection_db import db_init, write_data_in_collection, update_data_in_collection, get_data_from_collection
from scripts.comparer import Comparator

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris'
local_mod_path = F'{paradox_folder}\\mod\\local_localisation'
collection_path = f'{local_mod_path}\\collection.db'
stack_path = f'{local_mod_path}\\stack.json'
data = {}


def current_stellaris_version():
    with open(f'{paradox_folder}\settings.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if 'info' in line:
                current_version = f'{line[-5:-2]}.*'
    return current_version


def get_interface_lang():
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
        tool_language = f'GUI\\translations\\interface_{properties["tool_language"]}.qm'
    return tool_language


def thumbs_init(path="GUI\pictures\\thumbs"):
    if os.path.isdir(path) is False:
        os.mkdir(path)

    shutil.copy("GUI\pictures\\icons\\DoesNotExists.png", "GUI\pictures\\thumbs\\DoesNotExists.png")
    with open("GUI\pictures\\thumbs\\thumbs.json", "w", encoding="utf-8") as thumb:
        thumbnails = {}
        json.dump(thumbnails, thumb)


def properties_init():
    tool_language = getdefaultlocale()[0].split('_')[0]
    if tool_language not in ['en', 'ru', 'pl', 'uk', 'zh']:
        tool_language = 'en'
    with open('Properties.json', 'w', encoding='utf-8') as prop:
        properties = {
            "collection_name": "Stellaris True Machine Translation Tool",
            "tool_language": f"{tool_language}",
            "target_language": "en"
        }
        json.dump(properties, prop)


def local_mod_init():
    path_list = ['', '\\temp', '\\localisation', '\\common', '\\common\\name_lists', '\\common\\species_names']
    for folder in path_list:
        path = f'{local_mod_path}{folder}'
        if os.path.isdir(path) is False:
            os.mkdir(path)
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
    with open(f'{local_mod_path}.mod', 'w', encoding='utf-8') as mod:
        mod_description = f'name="{properties["collection_name"]}"' \
                          '\ntags={\n	"Translation"\n}' \
                          f'\npicture="thumbnail.png"' \
                          f'\nsupported_version="{current_stellaris_version()}"' \
                          f'\npath="{paradox_folder}\mod\local_localisation"'.replace('\\', '/')
        mod.write(mod_description)
    with open(f'{local_mod_path}\\descriptor.mod', 'w', encoding='utf-8') as descriptor:
        descriptor.write(mod_description.split('\npath=')[0])


def stack_init():
    with open(stack_path, 'w', encoding='utf-8') as stack:
        temp = []
        json.dump(temp, stack)


def generated_files_init():
    if os.path.isfile('Properties.json') is False:
        properties_init()
    if os.path.isfile(f'{local_mod_path}.mod') is False:
        local_mod_init()
    if os.path.isfile('GUI\pictures\\thumbs\\thumbs.json') is False:
        thumbs_init()
    if os.path.isfile(collection_path) is False:
        db_init(collection_path)
    if os.path.isfile(stack_path) is False:
        stack_init()


"""
                                ↓ Создание временных файлов ↓
"""


def open_zip_file(full_file_path):
    directory = '/'.join(full_file_path.split('\\')[:-1])
    with zipfile.ZipFile(full_file_path) as zip_file:
        zip_file.extractall(directory)


def remove_unpacked_files(mod_path):
    if list(filter(lambda x: '.zip' in x, os.listdir(mod_path))):
        directory = list(filter(lambda x: '.zip' not in x, os.listdir(mod_path)))
        folders, files = [], []
        for item in directory:
            if item.split('.')[-1] in '.txt.yml.yaml.mod.json.png.jpeg.jpg.mp.bin.py.db':
                files.append(item)
            else:
                folders.append(item)
        for item in files:
            os.remove(f'{mod_path}\\{item}')
        for item in folders:
            shutil.rmtree(f'{mod_path}\\{item}')


def scan_for_files(mod_path):
    # TODO simplify this code

    file_list = []

    folders_for_scan = ['localisation', ]
    if os.path.isdir(f'{mod_path}\\localisation') is True:
        for directory in folders_for_scan:
            scan = os.listdir(f'{mod_path}\\{directory}')
            folders = [folder for folder in scan if ".yml" not in folder and 'temp' not in folder]
            l_english = [file for file in scan if "l_english" in file and '.yml' in file]
            for folder in folders:
                folders_for_scan.append(f'{directory}\\{folder}')
            for file in l_english:
                file_list.append(f'{directory}\\{file}')

    folders_for_scan = ['common', ]
    if os.path.isdir(f'{mod_path}\\common') is True:
        for directory in folders_for_scan:
            scan = os.listdir(f'{mod_path}\\{directory}')
            folders = [folder for folder in scan if "name" in folder and '.txt' not in folder and 'temp' not in folder]
            name_list = [file for file in scan if '.txt' in file and 'random' not in file]
            for folder in folders:
                folders_for_scan.append(f'{directory}\\{folder}')
            for file in name_list:
                file_list.append(f'{directory}\\{file}')
    if not file_list:
        raise FileNotFoundError

    return file_list


def create_temp_folder(mod_id, file_path):
    temp_folder = f'{local_mod_path}\\temp\\{mod_id}'
    if os.path.isdir(temp_folder) is False:
        os.mkdir(temp_folder)
    for folder in file_path.split(".")[0].split('\\'):
        temp_folder += f'\\{folder}'
        if os.path.isdir(temp_folder) is False:
            os.mkdir(temp_folder)

    return temp_folder


def write_data_about_file(temp_folder, file_path):
    with open('Properties.json', 'r') as properties:
        properties = json.load(properties)
    data['target_language'] = LANGUAGES[properties["target_language"]]

    data["original_file_name"] = file_path.split("\\")[-1]
    data["original_file_path"] = f'{temp_folder}\\{data["original_file_name"]}'
    data["source_file_path"] = f'{temp_folder}\\source.txt'
    data["machine_file_path"] = f'{temp_folder}\\machine.txt'
    data["user_input_file_path"] = f'{temp_folder}\\user_input.txt'


def prepare_temp_files(machine_text):
    with open(data["machine_file_path"], 'w', encoding='utf-8') as machine:
        machine.write(''.join(machine_text))
    with open(data["user_input_file_path"], 'w', encoding='utf-8') as translator:
        translator.write(''.join(['\n'] * len(machine_text)))


def collection_append(mod_id, hashKey, mod_name):
    mod_info = {
        'mod_id': mod_id,
        'hash_key': hashKey,
        'mod_name': mod_name,
        'target_language': data['target_language'],
        'original_file_name': data['original_file_name'],
        'original_file_path': data['original_file_path'],
        'source_file_path': data['source_file_path'],
        'machine_file_path': data['machine_file_path'],
        'user_input_file_path': data['user_input_file_path'],
    }

    write_data_in_collection(collection_path, mod_info)


"""
                                ↓ Рендер ↓
"""


def get_collection_data():
    files = get_data_from_collection(collection_path)
    return files


def mod_name_wrap(mod_name, value):
    row = ['', '', '']
    special_symbols = {'&', }
    check = [symbol for symbol in special_symbols & set(mod_name)]
    if check:
        for symbol in check:
            mod_name = mod_name.replace(symbol, symbol * 2)
    if len(mod_name) > value:
        for word in mod_name.split():
            if len(f'{row[0]} {word}') < value:
                row[0] += f' {word}'
            else:
                row[0] += '\n'
                if not row[1]:
                    row[1] = row[0]
                else:
                    row[2] = row[0]
                row[0] = ''
                row[0] += f' {word}'
        mod_name = f'{row[1]}{row[2]}{row[0]}'

    return mod_name


def file_name_fix(original_name, option):
    parts = {
        '.yml': ['_l_'],
        '.txt': ['.txt'],
    }
    for part in parts[option]:
        original_name = original_name.split(part)[0]

    return mod_name_wrap(original_name.replace('_', ' ').replace('english', ''), 20)


def get_total_value(files):
    total_value = 0
    count = 0

    for file in files:
        total_value += file.tr_status
        count += 1

    total_value /= count
    return total_value


# TODO Доработать компоновку и стек
"""
                                ↓ Работа с локализациями ↓
"""


def open_file_for_resuming(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = [line for line in file]
    return text


def check_new_line_sym_ending(line):
    return line if line.endswith('\n') else line + '\n'


def save_stack(mod_id, file_name):
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack = json.load(stack_file)

    for elem in stack:  # Удаляет дубликаты
        if elem[1] == file_name:
            stack.remove(elem)

    stack.append((mod_id, file_name))
    with open(stack_path, 'w', encoding='utf-8') as stack_file:
        json.dump(stack, stack_file)


def collection_update(file, user_text):
    with open(file.user_input_file_path, 'w', encoding='utf-8') as user_input:
        user_input.write(''.join(user_text))

    update_data_in_collection(collection_path, file)
    save_stack(file.mod_id, file.original_file_name)


# def check_if_line_translated(orig_line, tr_line):
#     if orig_line.replace('\n', '').strip() == tr_line.replace('\n', '').strip():
#         return 'Извините, переводчик не смог перевести эту строку.\n'
#     else:
#         return tr_line


# def remove_extra_new_line_symbols(text):
#     while text[-1] == '\n':
#         text.pop()
#     return text


def get_info_from_stack():
    """
    :return: [(id, file_name)] последнего мода если стек заполнен или [] если стек пуст
    """
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack: list = json.load(stack_file)
    return stack[-1] if stack else stack


def compare(new, old):
    comparator = Comparator(new, old)
    result = comparator.comparing()
    data['compared'] = result
