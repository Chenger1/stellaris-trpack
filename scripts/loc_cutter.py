#!/usr/bin/python3
import re
import os

from scripts.utils import write_data_about_mode, create_temp_folder


def search(subs, line):
    match = subs.search(line)
    if match is not None:
        return 1
    else:
        return 0


def cutting_lines(temp_files):
    subs = re.compile(': |:0|:1|:"')

    orig_text = []
    for line in temp_files['loc']:
        if search(subs, line) == 1:
            if (line[0] and line[1]) != '#':
                a = line.find('"')
                lt = line[a + 1:-2]
                orig_text.append(lt + '\n')
                temp_files['cuttered'].write(lt + '\n')
            else:
                orig_text.append('\n')
                temp_files['cuttered'].write('\n')
        else:
            orig_text.append('\n')
            temp_files['cuttered'].write('\n')

    temp_files['loc'].close()
    temp_files['cuttered'].close()
    return orig_text


def creating_temp_files(loc_path, temp_folder):
    l_english = ''
    for path, folders, files in os.walk(loc_path):
        for file in files:
            path_to_file = os.path.join(path, file)
            if 'english' in path_to_file and '.yml' in path_to_file:
                l_english = path_to_file

    eng = l_english.split('\\')[-1]
    cutter = 'cutter_' + eng
    loc = open(l_english, 'r', encoding='utf-8')
    newloc = open(f'{temp_folder}\\{cutter}', 'w', encoding='utf-8')
    return {'english_name': eng,
            'cutter_file': cutter,
            'loc': loc,
            'cuttered': newloc}


def cutter_main(path, mod_id):
    loc_path = f'{path}\\localisation'
    temp_folder = create_temp_folder(mod_id, loc_path)
    temp_files = creating_temp_files(loc_path, temp_folder)
    write_data_about_mode(temp_folder, temp_files)
    orig_text = cutting_lines(temp_files)
    return orig_text
