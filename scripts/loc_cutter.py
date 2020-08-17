#!/usr/bin/python3
import re
import os

from scripts.utils import write_data_about_mode, create_temp_folder, data


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


def creating_temp_files(temp_folder):
    cutter = 'cutter_' + data['original_name']
    loc = open(data['full_path'], 'r', encoding='utf-8')
    newloc = open(f'{temp_folder}\\{cutter}', 'w', encoding='utf-8')
    return {'cutter_file': cutter,
            'loc': loc,
            'cuttered': newloc}


def cutter_main(path, mod_id):
    loc_path = f'{path}\\localisation'
    temp_folder = create_temp_folder(mod_id, loc_path)
    temp_files = creating_temp_files(temp_folder)
    write_data_about_mode(temp_folder, temp_files)
    orig_text = cutting_lines(temp_files)
    return orig_text
