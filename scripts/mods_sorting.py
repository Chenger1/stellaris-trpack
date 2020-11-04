"""
                              ↓ Инициализация данных ↓
"""

import json
from shutil import copyfile
import os
import errno

from scripts.utils import paradox_folder
from scripts.db import get_mods_from_playset, get_data_about_mods, write_data


def sortedKey(mod):
    return mod.sortedKey


def open_sorting_order_file():
    try:
        with open(f'{paradox_folder}\\mod\\local_localisation\\sorting_order.json', 'r', encoding='utf-8') as order:
            mod_data = json.load(order)
        return mod_data
    except FileNotFoundError:
        return {}


def checkIfSortRequired(m_list, playset):
    modListSort, modListNonSort = [], []
    mod_data = {}
    for mod in m_list:
        if mod.sortRequired is True:
            modListSort.append(mod)
        else:
            modListNonSort.append(mod)
        mod_data[mod.hash_key] = mod.sortRequired
    write_mod_sorting_order_in_json(playset, mod_data)
    return modListSort, modListNonSort


"""
                              ↓ Чтение данных ↓
"""


def getModList(mods_dict, enabled_mods, playset):
    modList = []
    try:
        mod_data = open_sorting_order_file()[playset[0]]
    except KeyError:
        mod_data = {}
    for hash_key, info in mods_dict.items():
        try:
            name = info['mod_name']
            mod_descritor = info['mod_descritor']
            isEnabled = True if hash_key in enabled_mods else False
            try:
                isSortingRequired = mod_data[hash_key]
            except KeyError:
                isSortingRequired = True
            mod = Mod(name, mod_descritor, hash_key, isEnabled, isSortingRequired,
                      info['position'])
            modList.append(mod)
        except KeyError:
            try:
                name = info['displayName']
                modId = info['steamId']
                isEnabled = True if hash_key in enabled_mods else False
                try:
                    isSortingRequired = mod_data[hash_key]
                except KeyError:
                    isSortingRequired = True
                mod = Mod(hash_key, name, modId, isEnabled, isSortingRequired,
                          info['position'])
                modList.append(mod)
            except KeyError:
                print('key not found in ')
    return sorted(modList, key=lambda x: x.position)


def prep_data(settings_path, playset):
    dlc_load = os.path.join(settings_path, 'dlc_load.json')
    copyfile(dlc_load, dlc_load + '.bak')

    game_data = os.path.join(settings_path, 'game_data.json')
    copyfile(game_data, game_data + '.bak')

    mods_id_tuple = get_mods_from_playset('get_mods_from_playset', playset[0])
    mods_data_dict = get_data_about_mods('get_mods_data_from_playset', mods_id_tuple)
    enabled_mods = [key for key, data in mods_data_dict.items() if data['isEnabled'] == 1]
    mod_list = getModList(mods_data_dict, enabled_mods, playset)

    return mod_list, game_data, dlc_load, playset


class Mod:
    def __init__(self, mod_name, mod_descritor, hash_key, isEnabled, isSortRequired, position):
        self.mod_name = mod_name
        self.mod_id = mod_descritor.split('_')[-1].split('.')[0]
        self.hash_key = hash_key
        self.checkboxes = [[0, 1]]
        self.sortRequired = isSortRequired
        self.isEnabled = isEnabled
        self.position = position
        self.sortedKey = mod_name.encode('ascii', errors='ignore')


"""
                              ↓ Сортировка списка модификаций ↓
"""


def tweakModOrder(m_list):
    for i in range(len(m_list) - 1, 0, -1):
        j = i - 1
        if m_list[j].sortedKey.startswith(m_list[i].sortedKey):
            tmp = m_list[j]
            m_list[j] = m_list[i]
            m_list[i] = tmp
    return m_list


def specialOrder(modListSort, modListNonSort):
    specialNames = ["UI Overhaul Dynamic", ]
    specialList = []
    for specialName in specialNames:
        toBeRemoved = []
        for mod in modListSort:
            if specialName in mod.mod_name:
                specialList.append(mod)
                toBeRemoved.append(mod)

        for mod in toBeRemoved:
            modListSort.remove(mod)
    return modListSort + specialList + modListNonSort


def sorting(modList, game_data, dlc_load, playset, reversing):
    positions = [elem.position for elem in modList]
    positions.sort()
    modListSort, modListNonSort = checkIfSortRequired(modList, playset[0])
    modListSort.sort(key=sortedKey, reverse=not reversing)
    # move Dark UI and UIOverhual to the bottom
    modList = specialOrder(modListSort, modListNonSort)
    # make sure UIOverhual+SpeedDial will load after UIOverhual
    modList = tweakModOrder(modList)
    for pos, mod in zip(positions, modList):
        mod.position = pos
    if len(modList) <= 0:
        return 'mods_not_found'
    idList = [mod.mod_id for mod in modList if mod.isEnabled is True]
    hashList = [mod.hash_key for mod in modList]
    writeDisplayOrder(hashList, game_data)
    writeLoadOrder(idList, dlc_load)
    write_data('write_data', modList, playset)
    return 'mods_was_sorted'


"""
                              ↓ Запись данных ↓
"""


def write_mod_sorting_order_in_json(playset_id, mod_data):
    sort_file = open_sorting_order_file()
    sort_file[playset_id] = mod_data
    with open(f'{paradox_folder}\\mod\\local_localisation\\sorting_order.json', 'w', encoding='utf-8') as file:
        json.dump(sort_file, file)


def writeLoadOrder(idList, dlc_load):
    with open(dlc_load, 'r+') as json_file:
        data = json.load(json_file)

    if len(data) < 1:
        raise FileNotFoundError('Ошибка загрузки dlc_load.json', errno.ENOENT, os.strerror(errno.ENOENT), dlc_load)

    data['enabled_mods'] = idList

    with open(dlc_load, 'w') as json_file:
        json.dump(data, json_file)


def writeDisplayOrder(hashList, game_data):
    try:
        with open(game_data, 'r+') as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError(pos=0, doc='', msg='Файл game_data.json пуст')

    data['modsOrder'] = hashList

    with open(game_data, 'w') as json_file:
        json.dump(data, json_file)
