#!/usr/bin/python3
import re

from scripts.utils import write_data_about_mode, create_temp_folder, data

file_dir = {'.yml': 'localisation',
            '.txt': 'common\\name_lists'
            }


def loc_search(subs, line):
    match = subs.search(line)
    if match is not None:
        return 1
    else:
        return 0


def name_search(subs, line):
    match = subs.search(line)
    if match is None:
        return 1
    else:
        return 0


def cutting_loc_lines(temp_file, file_path):
    subs = re.compile(': |:0|:1|:"')

    orig_text = []
    with open(file_path, 'r', encoding='utf-8') as loc:
        with open(temp_file, 'w', encoding='utf-8') as cuttered:
            for line in loc:
                if loc_search(subs, line) == 1:
                    if (line[0] and line[1]) != '#':
                        a = line.find('"')
                        lt = line[a + 1:-2]
                        orig_text.append(lt + '\n')
                        cuttered.write(lt + '\n')
                    else:
                        orig_text.append('\n')
                        cuttered.write('\n')
                else:
                    orig_text.append('\n')
                    cuttered.write('\n')

    return orig_text


def cutting_name_lines(temp_file, file_path):
    subs = re.compile('#|{|}')

    orig_text = []
    with open(file_path, 'r', encoding='utf-8') as loc:
        with open(temp_file, 'w', encoding='utf-8') as cuttered:
            for line in loc:
                if name_search(subs, line) == 1 and line[0] != '\n':
                    if '=' in line and '"' in line:
                        a = line.find('"')
                        lt = line[a + 1:-2].replace('%O%', '-th')
                        orig_text.append(lt + '\n')
                        cuttered.write(lt + '\n')
                    elif '=' not in line and '\t' not in line[-2]:
                        lt = line.replace('\t', '').replace('    ', '')
                        orig_text.append(lt)
                        cuttered.write(lt)
                    else:
                        orig_text.append('\n')
                        cuttered.write('\n')
                else:
                    orig_text.append('\n')
                    cuttered.write('\n')

    return orig_text


def creating_temp_files(temp_folder):
    cutter = 'cutter_' + data['original_name']
    r_data = {'cutter_file': cutter,
              'cuttered': f'{temp_folder}\\{cutter}'}
    return r_data


def cutter_main(path, mod_id, file_name, orig_text=[]):
    file_path = f'{path}\\{file_dir[data["original_name"][-4:]]}'
    temp_folder = create_temp_folder(mod_id, file_path, file_name)
    temp_files = creating_temp_files(temp_folder)
    write_data_about_mode(temp_files)
    if '.yml' in data["original_name"]:
        orig_text = cutting_loc_lines(temp_files['cuttered'], data['full_path'])
    elif '.txt' in data["original_name"]:
        orig_text = cutting_name_lines(temp_files['cuttered'], data['full_path'])
    return orig_text
