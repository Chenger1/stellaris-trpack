import json
import os
import re
import win32api

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
data = {}


def local_mod_status():
    mod_name = 'local_localisation'
    loc_mod_path = F'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris\\mod\\{mod_name}'
    try:
        with open(loc_mod_path + '.mod', 'r', encoding='utf-8') as mod:
            pass
    except FileNotFoundError:
        os.mkdir(loc_mod_path)
        os.mkdir(loc_mod_path + '\\localisation')
        with open(loc_mod_path + '.mod', 'w', encoding='utf-8') as mod:
            mod_description = 'version="2.7.*"\ntags={\n	"Translation"\n}\nname="Stellaris True Machine Translation ' \
                          'Tool"\nsupported_version="2.7.2"\npath=' + F'"{loc_mod_path}"'.replace('\\', '/')
            mod.write(mod_description)
        with open(loc_mod_path + '\\descriptor.mod', 'w', encoding='utf-8') as descriptor:
            descriptor.write(mod_description.split('path=')[0])


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


def paradox_mod_way_to_content(mod_id):
    ugc_id_mod = F'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris\\mod\\ugc_{mod_id}.mod'
    with open(ugc_id_mod, 'r', encoding='utf-8') as reading:
        for line in reading.readlines():
            if 'path' in line:
                path = line.split('"')[1].replace('/', '\\')
            if 'name' in line:
                name = line.split('"')[1].replace('/', '\\')
    return path, name


def get_mod_id(file_path):
    pattern = re.compile(r'281990/(.*?)/localisation')
    mod_id = pattern.findall(file_path)[0]
    return mod_id


def check_new_line_sym_ending(line):
    return line if line.endswith('\n') else line + '\n'


def check_if_line_translated(orig_line, tr_line):
    if orig_line.replace('\n', '').strip() == tr_line.replace('\n', '').strip():
        return 'Извините, переводчик не смог перевести эту строку'
    else:
        return tr_line
