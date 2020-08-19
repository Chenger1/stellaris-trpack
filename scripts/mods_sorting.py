# -*- coding: utf-8 -*-
#Mady by haifengkao
#https://github.com/haifengkao/StellairsLoadOrderFixer24/blob/master/load_order_stellaris24.py
import json
from shutil import copyfile
import os
import errno

from scripts.utils import paradox_folder
from scripts.db import get_mods_from_playset, get_data_about_mods, write_data


class Mod():
    def __init__(self, hashKey, name, modId, isEnabled, isSortRequired, position):
        self.hashKey = hashKey
        self.name = name
        self.modId = modId
        self.sortRequired = isSortRequired
        self.isEnabled = isEnabled
        self.position = position
        self.sortedKey = name.encode('ascii', errors='ignore')


def sortedKey(mod):
    return mod.sortedKey


def open_sorting_order_file():
    try:
        with open(f'{paradox_folder}\\mod\\local_localisation\\sorting_order.json', 'r', encoding='utf-8') as order:
            mod_data = json.load(order)
        return mod_data
    except FileNotFoundError:
        return {}


def write_mod_sorting_order_in_json(playset_id, mod_data):
    sort_file = open_sorting_order_file()
    sort_file[playset_id] = mod_data
    with open(f'{paradox_folder}\\mod\\local_localisation\\sorting_order.json', 'w', encoding='utf-8') as file:
        json.dump(sort_file, file)


def getModList(data, enabled_mods, playset):
    modList = []
    try:
        mod_data = open_sorting_order_file()[playset[0]]
    except KeyError:
        mod_data = {}
    for key, value in data.items():
        try:
            name = value['displayName']
            modId = value['gameRegistryId']
            isEnabled = True if key in enabled_mods else False
            try:
                isSortingRequired = mod_data[key]
            except KeyError:
                isSortingRequired = True
            mod = Mod(key, name, modId, isEnabled, isSortingRequired,
                      value['position'])
            modList.append(mod)
        except KeyError:
            try:
                name = value['displayName']
                modId = value['steamId']
                isEnabled = True if key in enabled_mods else False
                try:
                    isSortingRequired = mod_data[key]
                except KeyError:
                    isSortingRequired = True
                mod = Mod(key, name, modId, isEnabled, isSortingRequired,
                          value['position'])
                modList.append(mod)
            except KeyError:
                print('key not found in ')
    return sorted(modList, key=lambda x: x.position)


def sortModlist(m_list):
    modList = m_list.sort(key=sortedKey, reverse=True)
    return modList  # Todo


def checkIfSortRequired(m_list, playset):
    modListSort, modListNonSort = [], []
    mod_data = {}
    for mod in m_list:
        if mod.sortRequired is True:
            modListSort.append(mod)
        else:
            modListNonSort.append(mod)
        mod_data[mod.hashKey] = mod.sortRequired
    write_mod_sorting_order_in_json(playset, mod_data)
    return modListSort, modListNonSort


def tweakModOrder(m_list):
    for i in range(len(m_list) - 1, 0, -1):
        j = i - 1
        if m_list[j].sortedKey.startswith(m_list[i].sortedKey):
            tmp = m_list[j]
            m_list[j] = m_list[i]
            m_list[i] = tmp
    return m_list


def specialOrder(modListSort, modListNonSort):
    specialNames = ["UI Overhaul Dynamic", "Dark UI", "Dark U1"]
    specialList = []
    for specialName in specialNames:
        toBeRemoved = []
        for mod in modListSort:
            if specialName in mod.name:
                specialList.append(mod)
                toBeRemoved.append(mod)

        for mod in toBeRemoved:
            modListSort.remove(mod)
    return modListSort + specialList + modListNonSort


def writeLoadOrder(idList, dlc_load):
    data = {}
    with open(dlc_load, 'r+') as json_file:
        data = json.load(json_file)

    if len(data) < 1:
        raise FileNotFoundError('Ошибка загрузки dlc_load.json', errno.ENOENT, os.strerror(errno.ENOENT), dlc_load)

    data['enabled_mods'] = idList

    with open(dlc_load, 'w') as json_file:
        json.dump(data, json_file)


def writeDisplayOrder(hashList, game_data):
    data = {}
    try:
        with open(game_data, 'r+') as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError(pos=0, doc='', msg='Файл game_data.json пустой')

    data['modsOrder'] = hashList
    with open(game_data, 'w') as json_file:
        json.dump(data, json_file)


def prep_data(settingPath, playset):
    dlc_load = os.path.join(settingPath, 'dlc_load.json')
    copyfile(dlc_load, dlc_load + '.bak')

    game_data = os.path.join(settingPath, 'game_data.json')
    copyfile(game_data, game_data + '.bak')

    mods_id = get_mods_from_playset('get_mods_from_playset', playset[0])
    mods = get_data_about_mods('get_mods_data_from_playset', mods_id)
    enabled_mods = [key for key, data in mods.items() if data['isEnabled'] == 1]
    mod_list = getModList(mods, enabled_mods, playset)
    return mod_list, dlc_load, game_data, playset


def sorting(modList, game_data, dlc_load, playset):
    positions = [elem.position for elem in modList]
    positions.sort()
    modListSort, modListNonSort = checkIfSortRequired(modList, playset[0])
    modListSort.sort(key=sortedKey, reverse=True)
    # move Dark UI and UIOverhual to the bottom
    modList = specialOrder(modListSort, modListNonSort)
    # make sure UIOverhual+SpeedDial will load after UIOverhual
    modList = tweakModOrder(modList)
    for pos, mod in zip(positions, modList):
        mod.position = pos
    if len(modList) <= 0:
        return ('error', 'Моды не найдены')
    idList = [mod.modId for mod in modList if mod.isEnabled is True]
    hashList = [mod.hashKey for mod in modList]
    writeDisplayOrder(hashList, game_data)
    writeLoadOrder(idList, dlc_load)
    write_data('write_data', modList, playset)
    return ('success', 'Моды успешно отсортированы')


def set_settings():
    # check Stellaris settings location
    locations = [
        ".", "..",
        os.path.join(os.path.expanduser('~'), 'Documents', 'Paradox Interactive',
                     'Stellaris'),
        os.path.join(os.path.expanduser('~'), '.local', 'share',
                     'Paradox Interactive', 'Stellaris')
    ]
    settingPaths = [
        settingPath for settingPath in locations
        if os.path.isfile(os.path.join(settingPath, "launcher-v2.sqlite"))
    ]
    if settingPaths:
        return settingPaths
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                os.path.join(locations[2], "launcher-v2.sqlite"))
