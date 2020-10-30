"""
                              ↓ Инициализация данных ↓
"""

import sqlite3

from scripts.utils import paradox_folder

queries = {
    'get_mod_data':
        f'SELECT id, steamId, gameRegistryId, displayName FROM mods',
    'get_playset_list':
        f'SELECT id, name, isActive FROM playsets',
    'get_mods_from_playset':
        f'SELECT modId, enabled, position FROM playsets_mods WHERE playsetId=?',
    'get_mods_data_from_playset':
        f'SELECT steamId, gameRegistryId, displayName FROM mods WHERE id=? ',
    'write_data':
        f'UPDATE playsets_mods SET enabled=?, position=? WHERE modId=? AND playsetId=?',
    'get_path_to_mods':
        f'SELECT dirPath FROM mods',
    'get_mod_path':
        f'SELECT dirPath FROM mods WHERE displayName=?',
    'get_image_path':
        f'SELECT thumbnailUrl, thumbnailPath, steamId FROM mods WHERE id=?',
    'get_images':
        f'SELECT id, thumbnailPath, steamId FROM mods',
}


"""
                              ↓ Чтение данных ↓
"""


def get_data_about_mods(request, mods_id):
    data = {}
    with sqlite3.connect(f'{paradox_folder}\\launcher-v2.sqlite') as conn:
        cur = conn.cursor()
        for elem in mods_id:
            row_data = cur.execute(queries[request], (elem[0],)).fetchone()
            data[elem[0]] = {
                'mod_name': row_data[2],
                'steam_id': row_data[0],
                'mod_descritor': row_data[1],
                'isEnabled': elem[1],
                'position': elem[2]
            }
    return data


def get_mods_from_playset(request, playset_id, count=0):
    with sqlite3.connect(f'{paradox_folder}\\launcher-v2.sqlite') as conn:
        cur = conn.cursor()
        row_data = cur.execute(queries[request], (playset_id,))
        if count == 0:
            data = row_data.fetchall()
        elif count == 1:
            data = row_data.fetchone()
    return data


def get_info_from_db(request, count=0):
    with sqlite3.connect(f'{paradox_folder}\\launcher-v2.sqlite') as conn:
        cur = conn.cursor()
        row_data = cur.execute(queries[request])
        if count == 0:
            data = row_data.fetchall()
        elif count == 1:
            data = row_data.fetchone()
    return data


"""
                              ↓ Запись данных ↓
"""


def write_data(request, modList, playset):
    with sqlite3.connect(f'{paradox_folder}\\launcher-v2.sqlite') as conn:
        for mod in modList:
            conn.execute(queries[request], (mod.isEnabled, mod.position, mod.hash_key, playset[0]))
        conn.commit()
    return True


def write_data_into_db(request, data):
    with sqlite3.connect(f'{paradox_folder}\\launcher-v2.sqlite') as conn:
        conn.execute(queries[request], (data['image_path'], data['steam_id']))
        conn.commit()
    return True
