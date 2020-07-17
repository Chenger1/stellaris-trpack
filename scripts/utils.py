import json
import os
import re

STELLARIS = 'SteamLibrary\\steamapps\\workshop\\content\\281990\\'
data = {}


def create_temp_folder(mod_id, loc_path):
    temp_folder = f'{loc_path}\\{mod_id}_temp'
    data['folder_path'] = temp_folder
    data['base_dir'] = loc_path
    if os.path.isdir(f'{temp_folder}') is False:
        os.mkdir(temp_folder)
    return temp_folder


def creating_temp_files_names(original):
    return {'rus': 'rus_' + original,
            'translated': 'tr_' + original,
            'final': 'final_' + original}


def write_data_about_mode(temp_folder, temp_files):
    filenames = creating_temp_files_names(temp_files['english_name'])
    with open(f'{temp_folder}\\data.json', 'w') as d_file:
        json.dump({
            'folder_path': temp_folder,
            'cutter_file_name': filenames['rus'],
            'translated': filenames['translated'],
            'final': filenames['final']
        }, d_file)
    data['cutter_file_name'] = filenames['rus']
    data['translated_name'] = filenames['translated']
    data['final_name'] = filenames['final']
    data['original_name'] = temp_files['english_name']
    data['loc'] = temp_files['loc']
    data['cuttered'] = temp_files['cuttered']


def set_translated_file(file):
    data['translated_file'] = file


def get_mod_id(file_path):
    pattern = re.compile(r'281990\/(.*?)\/localisation')
    mod_id = pattern.findall(file_path)[0]
    return mod_id
