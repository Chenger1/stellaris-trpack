#!/usr/bin/python3
from googletrans import Translator
from langdetect import detect, DetectorFactory

import re
import json

from scripts.utils import data, set_translated_file


with open("Properties.json", 'r', encoding='utf-8') as prop:
	properties = json.load(prop)


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


def slice_string(line:str, specials={'§', '$', '£'}):
	result = []
	if '[' in line:
		pattern = re.compile(r'\[.*?\]')
	elif set(line) & specials:
		pattern = re.compile(r'[§$£].*?[§$£]')
	else:
		result.append(line)
		return result
	result = pattern.split(line)
	return result


def replacing_invalid_new_line_symbol(func):
	symbols = {
		'\ N \ n': '\\n\\n',
		'\ n \ n': '\\n\\n',
		'\ n': '\\n',
		'\ N': '\\n',
		'\ П': '\\n',
		'! \\n': '!\\n',
		'. \\n': '.\\n',
	}

	def wrapper(line, translator):
		ru_line = func(line, translator)
		for sym in symbols:
			ru_line = ru_line.replace(sym, symbols[sym])
		return ru_line
	return wrapper


@replacing_invalid_new_line_symbol
def translating_line(line: str, translator=None) -> str:
	translation = translator.translate(line, dest=properties["output_language"])
	return translation.text


def line_processing(line: str, translator) -> str:
	temp = slice_string(line)
	translated = list(map(lambda x: translating_line(x, translator), temp))
	for en, ru in zip(temp, translated):
		line = line.replace(en[:-1], ru)
	return line


def writing_translation(translation):
	with open(f"{data['folder_path']}\\{data['translated_name']}", 'w', encoding='utf-8') as translated:
		for line in translation:
			translated.write(line)
	set_translated_file(translated)


def defining_translator(func):
	translator = Translator()
	DetectorFactory.seed = 0

	def wrapper(line):
		ru_line = func(line, translator)
		return ru_line
	return wrapper


@defining_translator
def translate_line(line, translator=None):
	translation = ''
	if len(line) > 2:
		test = detect(line)
		if test != properties["output_language"]:
			translation = line_processing(line, translator)
		else:
			translation = line
	else:
		translation = line
	return translation
