#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import re
import os

def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def main():
	root = tk.Tk()
	root.withdraw()
	l_english = ''

												# ВАРИАНТ 1 --- УКАЗЫВАЕМ ФАЙЛ РУЧКАМИ
	# l_english = filedialog.askopenfilename() # указываем файл напрямую


										# ВАРИАНТ 2 --- УКАЗЫВАЕМ ССЫЛКУ НА МОД В STEAM WORKSHOP
	steam = ''
	steam_library = open('..\\path.txt', 'r+', encoding='utf-8')

	for path in steam_library:
		steam = path
		break

	stellaris = 'SteamLibrary\\steamapps\\workshop\\content\\281990\\'
	mod_id = input('Вставьте ссылку на установленный мод из SteamWorkshop или его id.\nНапример: https://steamcommunity.com/sharedfiles/filedetails/?id=1448888608\n').split('=')[-1]
	path = F'{steam}{stellaris}{mod_id}\\localisation'

	for path, folders, files in os.walk(path):
		for file in files:
			path_to_file = os.path.join(path, file)
			if 'english' in path_to_file and '.yml' in path_to_file:
				l_english = path_to_file

	eng = l_english.split('\\')[-1]
	rus = 'rus_' + eng
	file2 = l_english.replace(eng, rus)
	loc = open(l_english, 'r', encoding='utf-8')
	newloc = open(file2, 'w', encoding='utf-8')
	subs = re.compile(': |:0|:1|:"')

	for line in loc:
		if search(subs, line) == 1:
			if (line[0] and line[1]) != '#':
				a = line.find('"')
				lt = line[a + 1:-2]
				newloc.write(lt + '\n')
			else:
				newloc.write('\n')
		else:
			newloc.write('\n')

	loc.close()
	newloc.close()


if __name__ == "__main__":
	main()