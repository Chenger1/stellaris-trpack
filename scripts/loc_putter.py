#!/usr/bin/python3
import re
import shutil
import json

from itertools import islice

from googletrans.constants import LANGUAGES

from scripts.utils import data


def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def put_lines():
	file1 = data['loc'].name
	eng = data['original_name']
	neweng = data['final_name']
	file2 = data['translated_file'].name
	file3 = file1.replace(eng, neweng)
	loc = open(file1, 'r', encoding='utf-8')
	newloc = open(file2, 'r', encoding='utf-8')
	itog = open(f'{file3}.yml', 'w', encoding='utf-8')

	subs = re.compile(': |:0|:1|:"')
	trlist = []
	nonlist = []

	for line in newloc:
		trlist.append(line.rstrip())

	with open('Properties.json', 'r') as languages_json:
		languages = json.load(languages_json)
		itog.write(f'l_{LANGUAGES[languages["translation_language"]]}:\n')

	for index, line in enumerate(islice(loc, 1, None)):
		nonlist.append(line.rstrip())
		if (search(subs, line) == 1) and ((line[0] and line[1]) != '#'):
			a = line.find('"')
			curstr = line[0:a + 1] + trlist[index+1] + '"'
		else:
			curstr = nonlist[index]
		itog.write(curstr + '\n')

	loc.close()
	newloc.close()
	itog.close()
	shutil.rmtree(data['folder_path'])


if __name__ == "__main__":
	put_lines()
