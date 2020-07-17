#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import re
import os

from scripts.utils import write_data_about_mode, create_temp_folder, STELLARIS, data


def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def cutting_lines(temp_files):
	# root = tk.Tk()
	# root.withdraw()

	subs = re.compile(': |:0|:1|:"')

	for line in temp_files['loc']:
		if search(subs, line) == 1:
			if (line[0] and line[1]) != '#':
				a = line.find('"')
				lt = line[a + 1:-2]
				temp_files['cuttered'].write(lt + '\n')
			else:
				temp_files['cuttered'].write('\n')
		else:
			temp_files['cuttered'].write('\n')

	temp_files['loc'].close()
	temp_files['cuttered'].close()


def creating_temp_files(loc_path, temp_folder):
	l_english = ''
	for path, folders, files in os.walk(loc_path):
		for file in files:
			path_to_file = os.path.join(path, file)
			if 'english' in path_to_file and '.yml' in path_to_file:
				l_english = path_to_file

	eng = l_english.split('\\')[-1]
	rus = 'rus_' + eng
	loc = open(l_english, 'r', encoding='utf-8')
	newloc = open(f'{temp_folder}\\{rus}', 'w', encoding='utf-8')
	return {'english_name': eng,
			'cutter_file': rus,
			'loc': loc,
			'cuttered': newloc}


def finding_steam_library(stellaris, mod_id):
	steam = ''
	steam_library = open('path.txt', 'r+', encoding='utf-8')

	for path in steam_library:
		steam = path
		break
	loc_path = F'{steam}{stellaris}{mod_id}\\localisation'
	return loc_path


def cutter_main(mod_id):
	# ВАРИАНТ 1 --- УКАЗЫВАЕМ ФАЙЛ РУЧКАМИ
	# l_english = filedialog.askopenfilename() # указываем файл напрямую
	# ВАРИАНТ 2 --- УКАЗЫВАЕМ ССЫЛКУ НА МОД В STEAM WORKSHOP
	# mod_id = input(
	# 	'Вставьте ссылку на установленный мод из SteamWorkshop или его id.\nНапример: https://steamcommunity.com/sharedfiles/filedetails/?id=1448888608\n').split(
	# 	'=')[-1]
	loc_path = finding_steam_library(STELLARIS, mod_id)
	temp_folder = create_temp_folder(mod_id, loc_path)
	temp_files = creating_temp_files(loc_path, temp_folder)
	write_data_about_mode(temp_folder, temp_files)
	cutting_lines(temp_files)


if __name__ == '__main__':
	cutter_main(mod_id)