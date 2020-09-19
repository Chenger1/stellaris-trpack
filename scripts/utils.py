import json
import os
import re
import win32api
import zipfile
import shutil

from PyQt5 import QtWidgets, QtGui

from googletrans.constants import LANGUAGES

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris'
mod_path = F'{paradox_folder}\\mod\\local_localisation'
collection_path = f'{mod_path}\\collection.json'
version = '2.7.2'
data = {}


def local_mod_create():
    with open('Properties.json', 'r', encoding='utf-8') as prop:
        properties = json.load(prop)
    try:
        os.mkdir(mod_path)
        os.mkdir(mod_path + '\\localisation')
    except FileExistsError:
        pass
    with open(mod_path + '.mod', 'w', encoding='utf-8') as mod:
        mod_description = f'name="{properties["collection_name"]}"' + '\ntags={\n	"Translation"\n}' + f'\npicture="thumbnail.png"\nsupported_version="{version}"\npath="{paradox_folder}\mod\local_localisation"'.replace('\\', '/')
        mod.write(mod_description)
    with open(mod_path + '\\descriptor.mod', 'w', encoding='utf-8') as descriptor:
        descriptor.write(mod_description.split('path=')[0])


def local_mod_status():
    properties_status()
    try:
        with open(mod_path + '.mod', 'r', encoding='utf-8') as mod:
            pass
    except FileNotFoundError:
        local_mod_create()


def properties_create():
    with open('Properties.json', 'w', encoding='utf-8') as prop:
        properties = {"collection_name": "Stellaris True Machine Translation Tool", "tool_language": "en", "translation_language": "en"}
        json.dump(properties, prop)


def properties_status():
    try:
        with open('Properties.json', 'r', encoding='utf-8') as prop:
            pass
    except FileNotFoundError:
        properties_create()


def create_temp_folder(mod_id, loc_path):
    temp_folder = f'{loc_path}\\{mod_id}_temp'
    data['folder_path'] = temp_folder
    data['base_dir'] = loc_path
    if os.path.isdir(f'{data["folder_path"]}') is False:
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
    return {'path': path, 'name': name}


def init_collection():
    if os.path.isfile(collection_path) is False:
        with open(collection_path, 'w', encoding='utf-8') as collection:
            json.dump({}, collection)


def get_collection():
    try:
        with open(collection_path, 'r', encoding='utf-8') as collection:
            info = json.load(collection)
    except FileNotFoundError:
        with open(collection_path, 'w', encoding='utf-8') as collection:
            info = {}
            json.dump(info, collection)
    return info


def get_mod_info(mod_id, tr_status, pointer_pos, collection):
    name = data['mod_name']
    file_name = data['original_name']
    picture = "thumbnail.png"
    file_name_list = scan_for_localisations(mod_id)
    name_lists_list = scan_for_names(mod_id)
    file_tr_status_list = set_file_tr_status_list(file_name_list, file_name, tr_status, collection)
    name_list_tr_status_list = set_name_list_tr_status_list(name_lists_list, file_name, tr_status, collection)
    file_name_pointer_pos_list = set_file_name_pointer_pos_list(file_name_list, file_name, pointer_pos, collection)
    name_lists_pointer_pos_list = set_name_list_pointer_pos_list(name_lists_list, file_name, pointer_pos, collection)
    mod_info = {
        'mod_name': name,
        'picture': picture,
        'file_name_list': file_name_list,
        # 'file_name': file_name,

        # т.к. файл теперь может быть не один и лежаи они в списке, но путь к ним одинаковый, за исключением имени, надо что-то придумать
        'file_path': f'{paradox_folder}\\mod\\local_localisation\\localisation\\',
        # 'file_path': f'{paradox_folder}\\mod\\local_localisation\\localisation\\{data["final_name"]}',

        'name_lists_list': name_lists_list,
        'file_tr_status_list': file_tr_status_list,
        'name_list_tr_status_list': name_list_tr_status_list,
        'file_name_pointer_pos_list': file_name_pointer_pos_list,
        'name_lists_pointer_pos_list': name_lists_pointer_pos_list,
        # 'data': data
    }
    return mod_info


def collection_append(mod_id, tr_status, pointer_pos):
    with open(collection_path, 'r', encoding='utf-8') as collection:
        info = json.load(collection)
        try:
            mod_info = get_mod_info(mod_id, tr_status, pointer_pos, info[mod_id])
        except KeyError:
            mod_info = get_mod_info(mod_id, tr_status, pointer_pos, {})
        info[mod_id] = mod_info
    with open(collection_path, 'w', encoding='utf-8') as collection:
        json.dump(info, collection)


def get_mod_id(file_path):
    pattern = re.compile(r'281990/(.*?)/localisation')
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


def open_file_for_resuming(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = [line for line in file]
    return text


def remove_extra_new_line_symbols(text):
    while text[-1] == '\n':
        text.pop()
    return text


def set_button_style(button):
    button.setFont(QtGui.QFont("Arkhip", 9))
    button.setStyleSheet("""
            QPushButton{
            background-color: transparent;
            min-height: 40px;
            max-width: 400px;
            color: #ffffff;
            }
            QPushButton::hover {
            color: #05B8CC;
            }
            QPushButton::pressed {
            color: rgba(194, 194, 194, 50);
            }
            """)


def set_data_style(data_field):
    data_field.setFont(QtGui.QFont("Arkhip", 9))
    data_field.setReadOnly(True)
    data_field.setStyleSheet("""
                            QTextEdit{
                        background-color: transparent;
                        border: transparent;
                        max-width: 350px;
                        max-height: 70px;
                        color: #ffffff;
                        }
                            QTextEdit:hover{
                        color: #05B8CC;
                        }
                        """)


def set_incomplete_style(status):
    status.setFormat("%p%   ")
    status.setInvertedAppearance(True)
    status.setFont(QtGui.QFont("Arkhip", 9))
    status.setStyleSheet("""
                        QProgressBar{
                        background-color:  #1f2533;
                        border: solid grey;
                        border-radius: 10px;
                        color: white;
                        font-family: "KB Astrolyte";
                        text-align: right;
                        max-height: 20px;
                        max-width: 125;
                        margin-right: 10px;
                        }
                        QProgressBar::chunk {
                        background-color: #05B8CC;
                        border-radius :10px;
                        }      """)


def set_complete_style(status):
    status.setFormat("%p%   ")
    status.setInvertedAppearance(True)
    status.setFont(QtGui.QFont("Arkhip", 9))
    status.setStyleSheet("""
                        QProgressBar{
                        background-color: #1f2533;
                        border: solid grey;
                        border-radius: 10px;
                        color: white;
                        font-family: "KB Astrolyte";
                        text-align: right;
                        max-height: 20px;
                        max-width: 125;
                        margin-right: 10px;
                        }
                        QProgressBar::chunk {
                        background-color: #5abe41;
                        border-radius :10px;
                        }      """)


def create_separator():
    separator = QtWidgets.QTextEdit()
    separator.setStyleSheet("""
        QTextEdit {
            max-height: 0px;
            max-width: 100px;
            margin-right: 75px;
            border: 1px solid #05B8CC;
        }
        """)
    return separator


def scan_for_localisations(mod_id):
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
    with zipfile.ZipFile(file, 'r') as zip_file:
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
