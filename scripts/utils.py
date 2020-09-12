import json
import os
import re
import win32api
from PyQt5 import QtGui

from googletrans.constants import LANGUAGES

drive = win32api.GetSystemDirectory().split(':')[0]
user = win32api.GetUserName()
paradox_folder = f'{drive}:\\Users\\{user}\\Documents\\Paradox Interactive\\Stellaris'
collection_path = f'{paradox_folder}\\mod\\local_localisation\\collection.json'
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
            if 'name' in line:
                name = line.split('"')[1].replace('/', '\\')
                data['mod_name'] = name
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


def get_mod_info(pointer_pos, tr_status):
    name = data['mod_name']
    picture = "thumbnail.png"
    file_name = data['original_name']
    mod_info = {
        'name': name,
        'picture': picture,
        'file_name': file_name,
        # т.к. файл теперь может быть не один и лежит в списке, но путь к ним одинаковый за исключением имени, надо что-то придумать
        'file_path': f'{paradox_folder}\\mod\\local_localisation\\localisation\\',
        # 'file_path': f'{paradox_folder}\\mod\\local_localisation\\localisation\\{data["final_name"]}',

        # и вынести data в другой json
        # 'data': data,
        'tr_status': tr_status,
        'pointer_pos': pointer_pos
    }
    return mod_info


def collection_append(mod_id, pointer_pos, tr_status):
    mod_info = get_mod_info(pointer_pos, tr_status)
    with open(collection_path, 'r', encoding='utf-8') as collection:
        info = json.load(collection)
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
            text-align: left;            
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
    data_field.setStyleSheet("""
                            QLineEdit{
                        background-color: transparent;
                        border: transparent;
                        max-width: 250px;
                        color: #ffffff;
                        text-align: left;            
                        }
                            QLineEdit:hover{
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


def clean(grid):
    for i in reversed(range(grid.count())):
        grid.itemAt(i).widget().setParent(None)


def scaner():
    l_english = os.listdir('D:\Games\SteamLibrary\steamapps\workshop\content\\281990\\1067631798\localisation')
    if '.yml' not in l_english[0]:
        l_english = os.listdir('D:\Games\SteamLibrary\steamapps\workshop\content\\281990\\1067631798\localisation\english')
    return [l_english, ]
