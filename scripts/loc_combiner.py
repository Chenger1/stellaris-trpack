#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import re
import webbrowser


def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def checker(subs, line):
	if len(line) > 2:
		if ((line[0] and line[1]) != '#'):
			if search(subs, line) == 1:
				return 1


def main():
	root = tk.Tk()
	root.withdraw()
	file1 = filedialog.askopenfilename()
	eng = file1.split('/')[-1]
	rus = eng.replace('english', 'russian')
	spl = 'spl_' + eng
	file2 = file1.replace(eng, rus)
	file3 = file1.replace(eng, spl)
	original = open(file1, 'r', encoding='utf-8')
	translated = open(file2, 'r', encoding='utf-8')
	combined = open(file3, 'w', encoding='utf-8')
	subs = re.compile(': |:0|:1|:"')
	pairs = {}

	for line in translated:
		if checker(line, subs) == 1:
			a = line.find('"')
			ls = line[0:a].lstrip()
			rs = line[a:-1]
			pairs[ls] = rs

	for line in original:
		if checker(line, subs) == 1:
			a = line.find('"')
			ls = line[0:a].lstrip()
			newrs = pairs.get(ls)
			if newrs is not None:
				newrs = ls + newrs
				pairs.pop(ls)
				combined.write(newrs + '\n')
			else:
				combined.write(line)
		else:
			combined.write(line)

	webbrowser.open(file3)
	original.close()
	translated.close()
	combined.close()


if __name__ == "__main__":
	main()
