import json
import os
import re
import win32api

from googletrans.constants import LANGUAGES

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris\\mod'
data = {}


def local_mod_create(mod_path, name="Stellaris True Machine Translation Tool"):
    try:
        os.mkdir(mod_path)
        os.mkdir(mod_path + '\\localisation')
    except FileExistsError:
        pass
    with open(mod_path + '.mod', 'w', encoding='utf-8') as mod:
        mod_description = 'version="2.7.2"\ntags={\n	"Translation"\n}\nname=' + F'"{name}"\n' + \
                          'supported_version="2.7.2"\npath=' + F'"{mod_path}"'.replace('\\', '/')
        mod.write(mod_description)
    with open(mod_path + '\\descriptor.mod', 'w', encoding='utf-8') as descriptor:
        descriptor.write(mod_description.split('path=')[0])


def local_mod_status(mod_name="local_localisation"):
    mod_path = F'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris\\mod\\{mod_name}'
    try:
        with open(mod_path + '.mod', 'r', encoding='utf-8') as mod:
            pass
    except FileNotFoundError:
        local_mod_create(mod_path)


def local_mod_rename(name, mod_name="local_localisation"):
    mod_path = F'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris\\mod\\{mod_name}'
    local_mod_create(mod_path, name)


def create_temp_folder(mod_id, loc_path):
    temp_folder = f'{loc_path}\\{mod_id}_temp'
    data['folder_path'] = temp_folder
    data['base_dir'] = loc_path
    if os.path.isdir(f'{temp_folder}') is False:
        os.mkdir(temp_folder)
    return temp_folder


def creating_temp_files_names(original_file_name):
    mod_lang = list(filter(lambda x: x in original_file_name, LANGUAGES.values()))
    with open('Properties.json', 'r') as languages_json:
        languages = json.load(languages_json)
        files_names = {'cutter': 'cutter_' + original_file_name,
                       'translated': 'tr_' + original_file_name,
                       'final': original_file_name.replace(mod_lang[0], LANGUAGES[languages["translation_language"]])}
    return files_names


def write_data_about_mode(temp_folder, temp_files):
    filenames = creating_temp_files_names(temp_files['orig_name'])
    with open(f'{temp_folder}\\data.json', 'w') as d_file:
        json.dump({
            'folder_path': temp_folder,
            'cutter_file_name': filenames['cutter'],
            'translated': filenames['translated'],
            'final': filenames['final']
        }, d_file)
    data['cutter_file_name'] = filenames['cutter']
    data['translated_name'] = filenames['translated']
    data['final_name'] = filenames['final']
    data['original_name'] = temp_files['orig_name']
    data['loc'] = temp_files['loc']
    data['cuttered'] = temp_files['cuttered']


def set_translated_file(file):
    data['translated_file'] = file


def paradox_mod_way_to_content(mod_id):
    ugc_id_mod = f'{paradox_folder}\\ugc_{mod_id}.mod'
    with open(ugc_id_mod, 'r', encoding='utf-8') as reading:
        for line in reading.readlines():
            if 'path' in line:
                path = line.split('"')[1].replace('/', '\\')
            if 'name' in line:
                name = line.split('"')[1].replace('/', '\\')
    return {'path': path, 'name': name}


def get_collection():
    collection_path = f'{paradox_folder}\\local_localisation\\collection.json'
    try:
        with open(collection_path, 'r', encoding='utf-8') as collection:
            info = json.load(collection)
    except FileNotFoundError:
        with open(collection_path, 'w', encoding='utf-8') as collection:
            info = {}
            json.dump(info, collection)
    return info


def get_mod_info(mod_id):
    name = paradox_mod_way_to_content(mod_id)['name']
    picture = "thumbnail.png"
    status = "complete"
    mod_info = [name, picture, status]
    return mod_info


def collection_append(mod_id):
    collection_path = f'{paradox_folder}\\local_localisation\\collection.json'
    mod_info = get_mod_info(mod_id)
    with open(collection_path, 'r', encoding='utf-8') as collection:
        info = json.load(collection)
        info[mod_id] = mod_info
    with open(collection_path, 'w', encoding='utf-8') as collection:
        json.dump(info, collection)


def get_mod_id(file_path):
    pattern = re.compile(r'281990/(.*?)/localisation')
    mod_id = pattern.findall(file_path)[0]
    data['mod_name'] = file_path.split('/')[-1]
    data['full_path'] = file_path
    return mod_id


def check_new_line_sym_ending(line):
    return line if line.endswith('\n') else line + '\n'


def check_if_line_translated(orig_line, tr_line):
    if orig_line.replace('\n', '').strip() == tr_line.replace('\n', '').strip():
        return 'Извините, переводчик не смог перевести эту строку.'
    else:
        return tr_line
