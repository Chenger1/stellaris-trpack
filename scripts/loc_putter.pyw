#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import re
import shutil

from scripts.utils import data


def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def main():
	# root = tk.Tk()
	# root.withdraw()
	file1 = data['loc']
	eng = data['original_name']
	neweng = data['final_name']
	file2 = data['translated_file']
	file3 = file1.replace(eng, neweng)
	loc = open(file1, 'r', encoding='utf-8')
	newloc = open(file2, 'r', encoding='utf-8')
	itog = open(file3, 'w', encoding='utf-8')

	i = -1
	subs = re.compile(': |:0|:1|:"')
	trlist = []
	nonlist = []

	for line in newloc:
		trlist.append(line.rstrip())

	for line in loc:
		nonlist.append(line.rstrip())
		i += 1
		if (search(subs, line) == 1) and ((line[0] and line[1]) != '#'):
			a = line.find('"')
			curstr = line[0:a + 1] + trlist[i] + '"'
		else:
			curstr = nonlist[i]
		itog.write(curstr + '\n')

	loc.close()
	newloc.close()
	itog.close()
	shutil.rmtree(data['folder_path'])


if __name__ == "__main__":
	main()
