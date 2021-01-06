"""
                              ↓ Инициализация данных ↓
"""

from os import path, mkdir

from scripts.utils import local_mod_path
from copy import copy

from typing import Union, Tuple
from scripts.stack import Stack, NameListElement, LastParentStack

"""
                              ↓ Сохранение завершенной локализации ↓
"""


def put_lines(file):
    localisation_path_list = file.original_file_path.split(f'{file.mod_id}\\')[-1].split('\\')[0:-2]
    localisation_name = file.original_file_name.replace("english", file.target_language)
    localisation_path = f'{local_mod_path}'
    index = 0

    for folder in localisation_path_list:
        localisation_path += f'\\{folder}'
        if path.isdir(localisation_path) is False:
            mkdir(localisation_path)
    localisation_path += f'\\{localisation_name}'

    with open(file.original_file_path, 'r', encoding='utf-8') as original, \
            open(file.source_file_path, 'r', encoding='utf-8') as source, \
            open(file.user_input_file_path, 'r', encoding='utf-8') as user_input:
        original = original.readlines()
        source = source.readlines()
        user_input = user_input.readlines()

    with open(f"{localisation_path}", 'w', encoding='utf-8') as localisation:
        if file.type in 'localisation':
            original[0] = original[0].replace('l_english', f'l_{file.target_language}')
        localisation.write('\ufeff')

        for line in original:
            if ' +' in source[index]:
                while ' +' in source[index]:
                    line = line.replace(source[index][:-3], user_input[index][:-3])
                    index += 1
            else:
                if ':' in line:
                    line_parts = line.split(':', maxsplit=1)
                    line_parts[1] = line_parts[1].replace(source[index][:-1], user_input[index][:-1])
                    line = ':'.join(line_parts)
                else:
                    line = line.replace(source[index][:-1], user_input[index][:-1])
                index += 1
            localisation.write(line)


"""
                              ↓ Обновление файла ↓
"""


def index_dict(old_tr_text, new_ver_text, file_type):

    _index_dict = {index: None for index, var in enumerate(new_ver_text)}

    if file_type == 'localisation':
        new_ver_text_vars = [new_ver_line.split('"')[0] for new_ver_line in new_ver_text]
        old_tr_text_vars = [old_tr_line.split('"')[0] for old_tr_line in old_tr_text]
        for index in _index_dict:
            if new_ver_text_vars[index] in old_tr_text_vars:
                _index_dict[index] = old_tr_text_vars.index(new_ver_text_vars[index])
    else:
        _new_ver_text_parsed, _new_ver_text_instances = lists_parser(new_ver_text)
        _old_ver_text_parsed, _old_ver_text_instances = lists_parser(old_tr_text)
        _index_dict = comparing_lists(_new_ver_text_instances, _old_ver_text_instances, _index_dict)

    return _index_dict.items()


def comparing_lists(old_text: LastParentStack, new_text: LastParentStack, _index_dict: dict) -> dict:
    for instance in new_text:
        old_ver = list(filter(lambda old_ins: instance.full_path == old_ins.full_path, old_text))
        if len(old_ver) == 1:
            _index_dict[instance.index] = old_ver[0].index
        else:
            continue
    return _index_dict


def lists_parser(name_list: list) -> Tuple[dict, list]:
    brace_stack = Stack()
    last_parent_stack = LastParentStack()
    list_of_instances = []
    old_indexes = {}

    def _list_preparing(_name_list: list) -> list:
        res = []
        for index, line in enumerate(_name_list):
            line = _replace_symbols(line)
            if line == '':
                continue
            elif line.lstrip().startswith('#'):
                continue
            else:
                res.append(line)
                old_indexes[len(res)-1] = index
        return res

    def _replace_symbols(line: str) -> str:
        symbols = ['\n', '\t\t\n', '\t\n', '\t', '\ufeff',]
        for sym in symbols:
            if sym in line:
                line = line.replace(sym, '')
        return line

    def _check_statements(line: str) -> bool:
        if line.lstrip().startswith('#'):
            return True
        if not line.lstrip():
            return True
        return False

    def _create_new_instance_of_namelistelement(key: str, parent_key: str, index: int,
                                                full_path: str, value: Union[str, dict, list] = None) -> NameListElement:
        instance = NameListElement(key=key, parent_key=parent_key, index=index, value=value,
                                   full_path=full_path)
        list_of_instances.append(instance)
        return instance

    def _recursion_processing(_name_list: list, index: int = 0) -> Union[dict, tuple]:
        name_dict = {}
        list_of_elements = []
        while index <= len(_name_list)-1:
            line = _name_list[index]
            if _check_statements(line):
                index += 1
                continue

            if '{' in line and '}' in line:
                line = line.replace('{', '')
                line = line.replace('}', '')
                key, value = line.split('=', maxsplit=1)
                if '=' in value:
                    key1, value1 = value.split('=')
                    new_value = {key1: value1}
                    name_dict[key] = new_value
                    instance = _create_new_instance_of_namelistelement(key=key,
                                                                       parent_key=last_parent_stack.get_parent_key(),
                                                                       index=old_indexes[index], value=new_value,
                                                                       full_path=last_parent_stack.get_full_path(key))
                else:
                    name_dict[key] = value
                    instance = _create_new_instance_of_namelistelement(key=key,
                                                                       parent_key=last_parent_stack.get_parent_key(),
                                                                       index=old_indexes[index], value=value,
                                                                       full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)
                index += 1
                continue

            elif '{' in line:
                key, *_ = line.split('=')
                brace_stack.push('{')
                instance = _create_new_instance_of_namelistelement(key=key,
                                                                   parent_key=last_parent_stack.get_parent_key(),
                                                                   index=old_indexes[index],
                                                                   full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)

                last_parent_stack.push(instance)

                lines_ahead = []
                next_line = _name_list[index+1]
                if '=' not in next_line and '{' not in next_line and '}' not in next_line:
                    for i in range(index+1, len(_name_list)):
                        next_line = _name_list[i]

                        if '=' not in next_line and '{' not in next_line and '}' not in next_line:
                            lines_ahead.append(next_line)
                        else:
                            if '}' in next_line:
                                index = i+1
                            else:
                                index = i
                            name_dict[key] = lines_ahead
                            instance.value = lines_ahead
                            break
                    else:
                        name_dict[key] = lines_ahead
                        instance.value = lines_ahead
                else:
                    dictionary, index, child = _recursion_processing(_name_list, index+1)
                    #name_dict[key], index = recursion_processing(_name_list, index+1)
                    name_dict[key] = dictionary
                    instance.children.extend(child)

            elif '}' in line:
                brace_stack.pop()
                last_parent_stack.pop()
                return name_dict, index+1, list_of_elements
            elif '=' in line:
                key, value = line.split('=')
                instance = _create_new_instance_of_namelistelement(key=key,
                                                                   parent_key=last_parent_stack.get_parent_key(),
                                                                   index=old_indexes[index], value=value,
                                                                   full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)
                name_dict[key] = value
                index += 1
                continue
        else:
            return name_dict, index, list_of_elements

    text = _list_preparing(name_list)
    dictionary_of_parsed_name_list: dict = _recursion_processing(text)[0]
    return dictionary_of_parsed_name_list, list_of_instances


def update_lines(old_tr_file_path, new_ver_file_path):
    updated_file_path = old_tr_file_path.replace('.yml', '_updated.yml')
    file_type = 'localisation' if '.yml' in updated_file_path else '.txt'

    with open(old_tr_file_path, 'r', encoding='utf-8') as old_tr_text, \
            open(new_ver_file_path, 'r', encoding='utf-8') as new_ver_text:
        old_tr_text = old_tr_text.readlines()
        new_ver_text = new_ver_text.readlines()
    updated_text = copy(new_ver_text)

    for new_ver_index, old_tr_index in index_dict(old_tr_text, new_ver_text, file_type):
        try:
            if old_tr_index is not None:
                updated_text[new_ver_index] = old_tr_text[old_tr_index]
        except IndexError:
            break

    with open(f"{updated_file_path}", 'w', encoding='utf-8') as updated:
        updated.write(''.join(updated_text))
