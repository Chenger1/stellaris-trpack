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


def slicing_string(func):
	special = ('§', '$', '£')

	def wrapper(line: str, translator) -> str:
		counter = 0
		start_pos = end_pos = 0
		if search(special, line) != 0:
			for index, syb in enumerate(line):
				if syb in special:
					if counter == 0: start_pos = index
					if counter == 1: end_pos = index
					counter += 1
			slic = line[start_pos: end_pos + 1]
			temp = line.split(line[start_pos:end_pos + 1])
			translated_temp = list(map(lambda x: func(x, translator), temp))
			translated_line = slic.join(translated_temp)
		else:
			translated_line = func(line, translator)
		return translated_line
	return wrapper


@slicing_string
def translating_line(line: str, translator) -> str:
	translation = translator.translate(line, dest='ru')
	return translation.text


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
			if test != 'ru':
				translation = translating_line(line, translator)
				translation = translation + '\n'
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
