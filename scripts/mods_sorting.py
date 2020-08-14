# -*- coding: utf-8 -*-
#Mady by haifengkao
#https://github.com/haifengkao/StellairsLoadOrderFixer24/blob/master/load_order_stellaris24.py
import json
from shutil import copyfile
import os
import errno


class Mod():
    def __init__(self, hashKey, name, modId, isEnabled):
        self.hashKey = hashKey
        self.name = name
        self.modId = modId
        self.sortRequired = True
        self.isEnabled = isEnabled
        self.sortedKey = name.encode('ascii', errors='ignore')


def sortedKey(mod):
    return mod.sortedKey


def getModList(data, enabled_mods):
    modList = []
    for key, data in data.items():
        try:
            name = data['displayName']
            modId = data['gameRegistryId']
            isEnabled = True if modId in enabled_mods else False
            mod = Mod(key, name, modId, isEnabled)
            modList.append(mod)
        except KeyError:
            try:
                name = data['displayName']
                modId = data['steamId']
                isEnabled = True if modId in enabled_mods else False
                mod = Mod(key, name, modId, isEnabled)
                modList.append(mod)
            except KeyError:
                print('key not found in ', key, data)
    return modList


def sortModlist(m_list):
    modList = m_list.sort(key=sortedKey, reverse=True)
    return modList  # Todo


def checkIfSortRequired(m_list):
    modListSort, modListNonSort = [], []
    for mod in m_list:
        if mod.sortRequired is True:
            modListSort.append(mod)
        else:
            modListNonSort.append(mod)
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


def prep_data(settingPath):
    registry = os.path.join(settingPath, 'mods_registry.json')
    dlc_load = os.path.join(settingPath, 'dlc_load.json')
    copyfile(dlc_load, dlc_load + '.bak')

    enabled_mods = None
    try:
        with open(dlc_load) as dlc_load_file:
            dlc_load_data = json.load(dlc_load_file)

    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError(pos=0, doc='', msg='Файл dlc_load.json пустой')

    # Do some legwork ahead of time to put into a set to avoidic quadratic loop later for filtering.
    enabled_mods = frozenset(dlc_load_data.get("enabled_mods", []))

    game_data = os.path.join(settingPath, 'game_data.json')
    copyfile(game_data, game_data + '.bak')

    modList = []
    try:
        with open(registry, encoding='UTF-8') as json_file:
            data = json.load(json_file)
            modList = getModList(data, enabled_mods)
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError(pos=0, doc='', msg='Файл mods_registry.json пустой')

    return modList, dlc_load, game_data


def sorting(modList, game_data, dlc_load):
    modListSort, modListNonSort = checkIfSortRequired(modList)
    modListSort.sort(key=sortedKey, reverse=True)
    # move Dark UI and UIOverhual to the bottom
    modList = specialOrder(modListSort, modListNonSort)
    # make sure UIOverhual+SpeedDial will load after UIOverhual
    modList = tweakModOrder(modList)
    if len(modList) <= 0:
        return ('error', 'Моды не найдены')
    idList = [mod.modId for mod in modList if mod.isEnabled is True]
    hashList = [mod.hashKey for mod in modList]
    writeDisplayOrder(hashList, game_data)
    writeLoadOrder(idList, dlc_load)
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
        if os.path.isfile(os.path.join(settingPath, "mods_registry.json"))
    ]
    if settingPaths:
        return settingPaths
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                os.path.join(locations[2], "mods_registry.json"))
