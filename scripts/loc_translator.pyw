#!/usr/bin/python3
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from langdetect import detect, DetectorFactory
import webbrowser


def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1


def search(subs, line):
	counter = 0
	for i in range(len(subs)):
		if subs[i] in line:
			counter += 1
	if counter != 0:
		return 1
	else:
		return 0


def slice_string(line:str, specials={'§', '$', '£'}) -> list:
	words = []
	if set(line) & specials:
		start = end = 0
		counter = 0
		sym_stack = [False, '']
		while counter < len(line)-1:
			if line[counter] in specials:
				if line[counter] == sym_stack[1]:
					end = counter+1
					counter += 1
					sym_stack[0] = False
					sym_stack[1] = ''
				elif line[counter] in specials and sym_stack[0] is False:
					sym_stack[0] = True
					sym_stack[1] = line[counter]
					start = counter
					if line[end:start] not in (' ', ''): words.append(line[end:start])
					counter += 1
				else:
					counter += 1
			else:
				counter += 1
		else:
			if line[end:].strip() not in '!.': words.append(line[end:])
	else:
		words.append(line)
	return words


def translating_line(line: str, translator) -> str:
	translation = translator.translate(line, dest='ru')
	return translation.text


def flatten(a_list:list) -> list:
	temp = []
	for i in a_list:
		temp.extend(i)
	return temp


def line_processing(line: str, translator) -> str:
	split_temp = line.splitlines()
	split_temp = list(map(lambda x: x.split('\\n\\n'), split_temp))
	split_temp = flatten(split_temp)
	temp = list(map(lambda x: slice_string(x), split_temp))
	to_translate = flatten(temp)
	translated = list(map(lambda x: translating_line(x, translator), to_translate))
	temp = zip(to_translate, translated)
	translated_line = line
	for en, ru in temp:
		translated_line = translated_line.replace(en, ru)
	return translated_line


def main():
	translator = Translator()
	root = tk.Tk()
	root.withdraw()
	DetectorFactory.seed = 0
	file1 = filedialog.askopenfilename()
	eng = file1.split('/')[-1]
	rus = 'tr_' + eng[4:]
	file2 = file1.replace(eng, rus)
	loc = open(file1, 'r', encoding='utf-8')

	translated = open(file2, 'w', encoding='utf-8')

	for line in loc:
		translation = ''
		if len(line) > 2:
			test = detect(line)
			colons = line.count(':')
			if test != 'ru' and colons < 2:
				translation = line_processing(line, translator)
				#translation = translation + '\n'
				print(translation)
			else:
				translation = line
		else:
			translation = line
		translated.write(translation)

	#webbrowser.open(translated)
	loc.close()
	translated.close()


if __name__ == "__main__":
	main()
