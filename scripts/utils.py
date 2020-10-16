import json
import os
import re
import win32api
import zipfile
import shutil

from locale import getdefaultlocale
from googletrans.constants import LANGUAGES

from scripts.collection_db import create_db, write_data_in_collection, get_data_from_collection
from scripts.comparer import Comparator

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris'
mod_path = F'{paradox_folder}\\mod\\local_localisation'
collection_path = f'{mod_path}\\collection.db'
finished_folders_path = f'{mod_path}\\finished_translations'
stack_path = f'{mod_path}\\stack.json'
data = {}


def current_stellaris_version():
    with open(f'{paradox_folder}\settings.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if 'info' in line:
                current_version = f'{line[-5:-2]}.*'
    return current_version


def get_translation():
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
        tool_language = f'GUI\\translations\\interface_{properties["tool_language"]}.qm'
    return tool_language


def thumbs_create():
    os.mkdir("GUI\pictures\\thumbs")
    shutil.copy("GUI\pictures\\icons\\DoesNotExists.png", "GUI\pictures\\thumbs\\DoesNotExists.png")
    with open("GUI\pictures\\thumbs\\thumbs.json", "w", encoding="utf-8") as thumb:
        thumbnails = {}
        json.dump(thumbnails, thumb)


def properties_create():
    tool_language = getdefaultlocale()[0].split('_')[0]
    if tool_language not in ['en', 'ru', 'pl', 'uk', 'zh']:
        tool_language = 'en'
    with open('Properties.json', 'w', encoding='utf-8') as prop:
        properties = {"collection_name": "Stellaris True Machine Translation Tool", "tool_language": f"{tool_language}", "translation_language": "en"}
        json.dump(properties, prop)


def local_mod_create():
    try:
        os.mkdir(mod_path)
        os.mkdir(f'{mod_path}\\localisation')
        os.mkdir(f'{mod_path}\\common')
        os.mkdir(f'{mod_path}\\common\\name_lists')
        os.mkdir(f'{mod_path}\\common\\species_names')
        os.mkdir(f'{mod_path}\\finished_translations')
    except FileExistsError:
        pass
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
    with open(mod_path + '.mod', 'w', encoding='utf-8') as mod:
        mod_description = f'name="{properties["collection_name"]}"' + '\ntags={\n	"Translation"\n}' + f'\npicture="thumbnail.png"\nsupported_version="{current_stellaris_version()}"\npath="{paradox_folder}\mod\local_localisation"'.replace('\\', '/')
        mod.write(mod_description)
    with open(mod_path + '\\descriptor.mod', 'w', encoding='utf-8') as descriptor:
        descriptor.write(mod_description.split('path=')[0])


def init_stack():
    with open(stack_path, 'w', encoding='utf-8') as stack:
        temp = []
        json.dump(temp, stack)


def generated_files_status():
    if os.path.isfile('Properties.json') is False:
        properties_create()
    if os.path.isfile(f'{mod_path}.mod') is False:
        local_mod_create()
    if os.path.isfile('GUI\pictures\\thumbs\\thumbs.json') is False:
        thumbs_create()
    if os.path.isfile(collection_path) is False:
        create_db(collection_path)
    if os.path.isfile(stack_path) is False:
        init_stack()


def create_temp_folder(mod_id, file_path, file_name):
    temp_folder = f'{file_path}\\{mod_id}_{file_name}_temp'
    data['folder_path'] = temp_folder
    data['base_dir'] = file_path
    if os.path.isdir(f'{data["folder_path"]}') is False:
        os.mkdir(temp_folder)
    return temp_folder


# TODO add name-list support

def creating_temp_files_names(original_file_name):
    # if '.txt' in original_file_name:
    #     original_file_name = original_file_name.replace('.', '_english.')
    mod_lang = list(filter(lambda x: x in original_file_name, LANGUAGES.values()))
    with open('Properties.json', 'r') as languages_json:
        languages = json.load(languages_json)
        files_names = {'cutter': 'cutter_' + original_file_name,
                       'translated': 'tr_' + original_file_name,
                       'final': original_file_name.replace(mod_lang[0], LANGUAGES[languages["translation_language"]])}
        data['language'] = LANGUAGES[languages["translation_language"]]
    return files_names


def write_data_about_mode(temp_files):
    filenames = creating_temp_files_names(data['original_name'])
    data['cutter_file_name'] = filenames['cutter']
    data['translated_name'] = filenames['translated']
    data['final_name'] = filenames['final']
    data['cuttered'] = temp_files['cuttered']


def set_translated_file(file):
    data['translated_file'] = file


def paradox_mod_way_to_content(mod_id):
    ugc_id_mod = f'{paradox_folder}\\mod\\ugc_{mod_id}.mod'
    with open(ugc_id_mod, 'r', encoding='utf-8') as reading:
        for line in reading.readlines():
            if 'path' in line:
                path = line.split('"')[1].replace('/', '\\')
            elif 'name' in line:
                name = line.split('"')[1].replace('/', '\\')
                data['mod_name'] = name
            elif 'archive' in line:
                pre_path = line.split('"')[1]
                path = '\\'.join(pre_path.split('/')[:-1])

    result = {'path': path,
              'name': name}

    try:
        original_name = data['original_name']
        if '.yml' in original_name:
            original_name = original_name.split('.yml')[0]
        elif '.txt' in original_name:
            original_name = original_name.split('.txt')[0]
        result['file_name'] = original_name
    except KeyError:
        pass

    return result


def get_collection():
    info = get_data_from_collection(collection_path)
    return info


def save_stack(mod_id, file_name):
    with open(stack_path, 'r', encoding='utf-8') as stack_file:
        stack = json.load(stack_file)

    for elem in stack:  # Удаляет дубликаты
        if elem[1] == file_name:
            stack.remove(elem)

    stack.append((mod_id, file_name))
    with open(stack_path, 'w', encoding='utf-8') as stack_file:
        json.dump(stack, stack_file)


def get_mod_info(mod_id, tr_status, pointer_pos, hashKey):
    name = data['mod_name']
    file_name = data['original_name'] if tr_status == 0 else data['final_name']
    picture = "thumbnail.png"
    file_name_list = scan_for_localisations(mod_id, file_name) + scan_for_names(mod_id)
    mod_info = {
        'mod_id': mod_id,
        'file_name': file_name,
        'picture': picture,
        'file_tr_status': tr_status,
        'name_list_tr_status': 0,
        'file_name_pointer_pos': pointer_pos,
        'name_list_pointer_pos': 0,
        'language': data['language'],
        'original_name': data['original_name'],
        'full_path': data['full_path'],
        'mod_name': name,
        'folder_path': data['folder_path'],
        'cutter_file_name': data['cutter_file_name'],
        'translated_name': data['translated_name'],
        'cuttered': data['cuttered'],
        'translated_file': data['translated_file'],
        'machine_text': data['machine_text'],
        'status': 'mod_file',
        'base_dir': data['base_dir'],
        'id': hashKey
    }
    return mod_info, file_name_list, file_name


def collection_append(mod_id, tr_status, pointer_pos, hashKey):
    """
    *mod_info, name -  означает что из функции get_mod_info произойдет распаковка значений
    в следующем порядке:
        mod_info = [mod_info, file_name_list, name_lists_list]
        name = file_name
    """
    *mod_info, name = get_mod_info(mod_id, tr_status, pointer_pos, hashKey)
    save_stack(mod_id, name)
    write_data_in_collection(collection_path, mod_info)


def get_mod_id(file_path):
    pattern = re.compile(r'281990/(.*?)/')
    mod_id = pattern.findall(file_path)[0]
    data['original_name'] = file_path.split('/')[-1]
    data['full_path'] = file_path
    return mod_id


def check_new_line_sym_ending(line):
    return line if line.endswith('\n') else line + '\n'


def check_if_line_translated(orig_line, tr_line):
    if orig_line.replace('\n', '').strip() == tr_line.replace('\n', '').strip():
        return 'Извините, переводчик не смог перевести эту строку.\n'
    else:
        return tr_line


def save_unfinished_machine_text(mac_text):
    with open(f'{data["folder_path"]}\\machine_text.txt', 'w', encoding='utf-8') as file:
        for line in mac_text:
            file.write(line)
        data['machine_text'] = file.name


def set_data(resume):
    data['original_name'] = resume['original_name']
    data['full_path'] = resume['full_path']
    data['mod_name'] = resume['mod_name']
    data['folder_path'] = resume['folder_path']
    data['base_dir'] = resume['base_dir']
    data['cutter_file_name'] = resume['cutter_file_name']
    data['translated_name'] = resume['translated_name']
    data['final_name'] = resume['final_name']
    data['cuttered'] = resume['cuttered']
    data['translated_file'] = resume['translated_file']
    data['machine_text'] = resume['machine_text']
    data['language'] = resume['language']


def open_file_for_resuming(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = [line for line in file]
    return text


def remove_extra_new_line_symbols(text):
    while text[-1] == '\n':
        text.pop()
    return text


# TODO add name-list support

def scan_for_localisations(mod_id, file_name):
    folders_for_scan = ['', ]
    l_english_list = []
    for directory in folders_for_scan:
        path = f'{paradox_mod_way_to_content(mod_id)["path"]}\\localisation{directory}'
        scan = os.listdir(path)
        folders = [folder for folder in scan if ".yml" not in folder and 'temp' not in folder]
        l_english = [file for file in scan if "l_english" in file and '.yml' in file]
        try:
            for folder in folders:
                folders_for_scan.append(f'{directory}\\{folder}')
            for file in l_english:
                l_english_list.append(file)
        except IndexError:
            pass
    if '_l_english' not in file_name:
        l_english_list[l_english_list.index(data['original_name'])] = file_name
    return l_english_list


def scan_for_names(mod_id):
    try:
        path = f'{paradox_mod_way_to_content(mod_id)["path"]}\\common\\name_lists'
        name_lists_list = os.listdir(path)
    except FileNotFoundError:
        name_lists_list = []
    return name_lists_list


def set_file_tr_status_list(file_name_list, file_name, tr_status, collection):
    count = len(file_name_list)
    try:
        file_tr_status_list = collection["file_tr_status_list"]
    except KeyError:
        file_tr_status_list = []
    while len(file_tr_status_list) != count:
        file_tr_status_list.append(0)
    if '.yml' in file_name:
        file_tr_status_list[file_name_list.index(file_name)] = tr_status
    return file_tr_status_list


def set_name_list_tr_status_list(name_lists_list, file_name, tr_status, collection):
    count = len(name_lists_list)
    try:
        name_list_tr_status_list = collection["name_list_tr_status_list"]
    except KeyError:
        name_list_tr_status_list = []
    while len(name_list_tr_status_list) != count:
        name_list_tr_status_list.append(0)
    if '.txt' in file_name:
        name_list_tr_status_list[name_lists_list.index(file_name)] = tr_status
    return name_list_tr_status_list


def set_file_name_pointer_pos_list(file_name_list, file_name, pointer_pos, collection):
    count = len(file_name_list)
    try:
        file_name_pointer_pos_list = collection["file_name_pointer_pos_list"]
    except KeyError:
        file_name_pointer_pos_list = []
    while len(file_name_pointer_pos_list) != count:
        file_name_pointer_pos_list.append(0)
    if '.yml' in file_name:
        file_name_pointer_pos_list[file_name_list.index(file_name)] = pointer_pos
    return file_name_pointer_pos_list


def set_name_list_pointer_pos_list(name_lists_list, file_name, pointer_pos, collection):
    count = len(name_lists_list)
    try:
        name_list_pointer_pos_list = collection["name_list_pointer_pos_list"]
    except KeyError:
        name_list_pointer_pos_list = []
    while len(name_list_pointer_pos_list) != count:
        name_list_pointer_pos_list.append(0)
    if '.txt' in file_name:
        name_list_pointer_pos_list[name_lists_list.index(file_name)] = pointer_pos
    return name_list_pointer_pos_list


def open_zip_file(file):
    directory = '/'.join(file.split('/')[:-1])
    with zipfile.ZipFile(file) as zip_file:
        zip_file.extractall(directory)


def remove_unpacked_files():
    path = data['base_dir'].split('\\localisation')[0]
    if list(filter(lambda x: '.zip' in x, os.listdir(path))):
        directory = list(filter(lambda x: '.zip' not in x, os.listdir(path)))
        folders, files = [], []
        for item in directory:
            if item.split('.')[-1] in '.txt.yml.yaml.mod.json.png.jpeg.jpg.mp.bin.py.db':
                files.append(item)
            else:
                folders.append(item)
        for item in files:
            os.remove(f'{path}\\{item}')
        for item in folders:
            shutil.rmtree(f'{path}\\{item}')


def mod_name_wrap(mod_name):
    row = ['', '', '']
    special_symbols = {'&', }
    check = [symbol for symbol in special_symbols & set(mod_name)]
    if check:
        for symbol in check:
            mod_name = mod_name.replace(symbol, symbol * 2)
    if len(mod_name) > 50:
        for word in mod_name.split():
            if len(f'{row[0]} {word}') < 50:
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


def move_folder():
    try:
        new_folder_path = shutil.move(data['folder_path'], finished_folders_path)
        data['folder_path'] = new_folder_path
        data['cuttered'] = f'{new_folder_path}\\{data["cutter_file_name"]}'
        data['translated_file'] = f'{new_folder_path}\\{data["translated_name"]}'
        data['machine_text'] = f'{new_folder_path}\\machine_text.txt'
    except shutil.Error:
        return None


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


def get_info_from_data(key):
    try:
        return data[key]
    except KeyError:
        return False
