"""
                                ↓ Инициализация основных файлов и данных ↓
"""

import json
import os
import zipfile
import shutil
import glob

from win32api import GetSystemDirectory, GetUserName
from locale import getdefaultlocale
from googletrans.constants import LANGUAGES

from scripts.db import set_collection_data, get_info_from_db
from scripts.collection_db import db_init, write_data_in_collection, update_data_in_collection, get_data_from_collection
# from scripts.comparer import Comparator
from scripts.pictures import thumbs_synchronize

drive = GetSystemDirectory().split(':')[0]
user = GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris'
local_mod_path = F'{paradox_folder}\\mod\\local_localisation'

# TODO Попытаться брать hash мода из бд, например, по признаку local_mod и RegistryID
collection_hash = '6fdfef4b-b06d-42fc-897f-b922efcd534b'

collection_path = f'{local_mod_path}\\collection.db'
collection_tumbnail_path = f'{paradox_folder}\\.launcher-cache\\_local-mod-thumbnail-collection_ru\\{collection_hash}.png'
stack_path = f'{local_mod_path}\\stack.json'
temp_folder_path = f'{local_mod_path}\\temp'
data = {}


def current_stellaris_version():
    with open(f'{paradox_folder}\\settings.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if 'info' in line:
                current_version = f'{line[-5:-2]}.*'

    return current_version


def get_interface_lang():
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
        tool_language = f'GUI\\translations\\interface_{properties["tool_language"]}.qm'

    return tool_language


def set_collection_mod_thumbnail():
    local_mod_thumbnails_path = 'GUI\\pictures\\icons\\local_mod_thumbnails'
    with open('Properties.json', 'r', encoding='utf-8') as properties:
        properties = json.load(properties)
        target_language = properties["target_language"]

    collection_thumbs_dir = collection_tumbnail_path.split(f'\\{collection_hash}')[0]
    if os.path.isdir(collection_thumbs_dir) is False:
        os.mkdir(collection_thumbs_dir)

    if os.path.isdir(local_mod_thumbnails_path) is True:
        thumbnails = os.listdir(local_mod_thumbnails_path)
        for thumbnail in thumbnails:
            if target_language in thumbnail:
                shutil.copyfile(f'{local_mod_thumbnails_path}\\{thumbnail}', collection_tumbnail_path)
                shutil.copyfile(collection_tumbnail_path, f'{local_mod_path}\\thumbnail.png')
                set_collection_data('set_collection_thumbnail', (collection_tumbnail_path, collection_hash))
                break


def thumbs_init(path="GUI\pictures\\thumbs"):
    if os.path.isdir(path) is False:
        os.mkdir(path)

    shutil.copy("GUI\pictures\\icons\\DoesNotExists.png", "GUI\pictures\\thumbs\\DoesNotExists.png")
    with open("GUI\pictures\\thumbs\\thumbs.json", "w", encoding="utf-8") as thumb:
        thumbnails = {}
        json.dump(thumbnails, thumb)


def collection_settings_update(settings):
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
        properties["collection_name"] = settings[0]
    with open("Properties.json", 'w', encoding='utf-8') as prop:
        json.dump(properties, prop)

    set_collection_data('collection_settings_update', settings)

    local_mod_init()


def properties_init():
    tool_language = getdefaultlocale()[0].split('_')[0]
    if tool_language not in ['en', 'ru', 'pl', 'uk', 'zh']:
        tool_language = 'en'

    with open('Properties.json', 'w', encoding='utf-8') as prop:
        properties = {
            "collection_name": "Stellaris True Machine Translation Tool",
            "tool_language": f"{tool_language}",
            "target_language": "ru"
        }
        json.dump(properties, prop)


def local_mod_init():
    path_list = ['', '\\temp']
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

    set_collection_mod_thumbnail()


def stack_init():
    with open(stack_path, 'w', encoding='utf-8') as stack:
        temp = []
        json.dump(temp, stack)


def generated_files_init():
    if os.path.isfile('Properties.json') is False:
        properties_init()

    if os.path.isfile(f'{local_mod_path}.mod') is False or \
            os.path.isfile(f'{local_mod_path}\\local_localisation\\descriptor.mod') is False:
        local_mod_init()

    if os.path.isfile('GUI\pictures\\thumbs\\thumbs.json') is False:
        thumbs_init()

    if os.path.isfile(collection_path) is False:
        db_init(collection_path)

    if os.path.isfile(stack_path) is False:
        stack_init()

    if os.path.isdir(temp_folder_path) is False:
        os.mkdir(temp_folder_path)

    thumbs_synchronize()


"""
                                ↓ Создание временных файлов ↓
"""


def open_zip_file(full_file_path):
    directory = '/'.join(full_file_path.split('\\')[:-1])
    with zipfile.ZipFile(full_file_path) as zip_file:
        zip_file.extractall(directory)


def remove_unpacked_files(mod_path):
    if glob.glob(f'{mod_path}\\*.zip'):
        for item in os.listdir(mod_path):
            item_path = f'{mod_path}\\{item}'
            if '.zip' in item:
                continue
            elif os.path.isdir(item_path) is True:
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path) is True:
                os.remove(item_path)
            else:
                continue


def scan_for_files(mod_path):
    path_list = ['localisation', 'common', ]
    file_list = []

    for path in path_list:
        folders_for_scan = [path, ]
        for directory in folders_for_scan:
            if os.path.isdir(f'{mod_path}\\{directory}') is True:
                scan = os.listdir(f'{mod_path}\\{directory}')

                folders = [folder for folder in scan if ".yml" not in folder] if folders_for_scan[0] == 'localisation' \
                    else [folder for folder in scan if ".txt" not in folder and "name" in folder]
                files = [file for file in scan if "l_english" in file and '.yml' in file] if folders_for_scan[0] == 'localisation' \
                    else [file for file in scan if '.txt' in file and 'random' not in file]

                for folder in folders:
                    folders_for_scan.append(f'{directory}\\{folder}')
                for file in files:
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
    with open(data["user_input_file_path"], 'w', encoding='utf-8') as user_input:
        user_input_text = ''.join(['\n'] * len(machine_text))[0:-1] + ' '
        user_input.write(user_input_text)


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
    rows = ['', '', '', '', '']
    special_symbols = {'&', }
    check = [symbol for symbol in special_symbols & set(mod_name)]
    if check:
        for symbol in check:
            mod_name = mod_name.replace(symbol, symbol * 2)
    if len(mod_name) > value:
        for word in mod_name.split():
            if len(f'{rows[0]} {word}') < value:
                rows[0] += f' {word}'
            else:
                rows[0] += '\n'
                for index, row in enumerate(rows):
                    if not row:
                        rows[index] = rows[0]
                        rows[0] = f' {word}'
                        break

        mod_name = f'{rows[1]}{rows[2]}{rows[3]}{rows[0]}'

    return mod_name


def file_name_fix(original_name, option):
    parts = {
        'localisation': ['_l_'],
        'name_lists': ['.txt'],
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


def get_collection_description(collection_name, prescripted_description, mod_list):
    description = get_info_from_db('get_collection_description', (collection_name,), count=1)[0]
    if mod_list in description:
        description = description.split(f'\n\n{mod_list}')[0]

    if not description or description == '':
        description = prescripted_description

    return description


def get_collection_mod_list(collection, mod_list):
    mod_list = [f'\n{mod_list}\n', ]
    for mod_id, files in collection:
        mod_list.append(f'{files[0].mod_name}\n')
    mod_list = '\n'.join(mod_list)
    return mod_list


"""
                                ↓ Работа с локализациями ↓
"""


def open_file_for_resuming(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = [line for line in file]
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='windows-1252') as file:
            text = [line for line in file]

    return text


def check_new_line_sym_ending(line):
    return line if line.endswith('\n') else line + '\n'


def save_stack(mod_id, file_name):
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack = json.load(stack_file)

    for file in stack:  # Удаляет дубликаты
        if file[1] == file_name:
            stack.remove(file)

    stack.append((mod_id, file_name))
    with open(stack_path, 'w', encoding='utf-8') as stack_file:
        json.dump(stack, stack_file)


def pop_stack():
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack = json.load(stack_file)
        stack.pop(-1)

    with open(stack_path, 'w', encoding='utf-8') as stack_file:
        json.dump(stack, stack_file)


def collection_update(file, user_text):
    with open(file.user_input_file_path, 'w', encoding='utf-8') as user_input:
        user_input.write(''.join(user_text.pop() + ' '))

    update_data_in_collection(collection_path, file)
    save_stack(file.mod_id, file.original_file_name)


def remove_extra_new_line_symbols(source_text, source_file_path):
    if source_text[-1] == '\n':
        source_text[-1] = ' '
        with open(source_file_path, 'w') as fixed:
            fixed.write(''.join(source_text))

    return source_text


def find_last_file(collection, last_file):
    """
                Поиск последнего переводимого файла в коллекции
                для продолжения локализации
    """
    for file in collection[last_file[0]]:
        if file.original_file_name == last_file[1]:
            return file


def get_info_from_stack():
    """
    :return: [(id, file_name)] последнего мода если стек заполнен или [] если стек пуст
    """
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack: list = json.load(stack_file)

    return stack[-1] if stack else stack

# def compare(new, old):
#     comparator = Comparator(new, old)
#     result = comparator.comparing()
#     data['compared'] = result
