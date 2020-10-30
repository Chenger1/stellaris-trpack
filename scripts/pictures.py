"""
                            ↓ Инициализация данных ↓
"""

from PIL import Image
from json import load, dump
from os import remove, path
from copy import copy

from scripts.db import get_info_from_db

output_path = 'GUI\pictures\\thumbs\\'
images = {elem[0]: elem[1] for elem in get_info_from_db('get_images')}


"""
                            ↓ Работа с изображениями ↓
"""


def get_thumbnail(hash_key):
    try:
        with open(f'{output_path}\\thumbs.json', 'r', encoding='utf-8') as thumb:
            thumbnails = load(thumb)
        return thumbnails[hash_key]
    except KeyError:
        return f'{output_path}DoesNotExists.png'


def thumbs_synchronize():
    with open(f'{output_path}thumbs.json', 'r', encoding='utf-8') as thumbs:
        thumbnails = load(thumbs)
        scan = copy(thumbnails)
    for hash_key in scan:
        if hash_key not in images:
            del thumbnails[hash_key]
            remove(f'{output_path}{hash_key}.png')
    with open(f'{output_path}thumbs.json', 'w', encoding='utf-8') as thumb:
        dump(thumbnails, thumb)

    for hash_key, cache_path in images.items():
        if hash_key not in thumbnails or path.isfile(cache_path) is False:
            try:
                scale_image(hash_key, cache_path)
            except FileNotFoundError:
                pass
            except AttributeError:
                pass


def scale_image(hash_key, cache_path):
    size = (160, 100)
    original_image = Image.open(cache_path)
    width, height = original_image.size

    if width - height > 200:
        setting = (0, 0, height * 1.6, height)
        original_image = original_image.crop(setting)
    elif width >= height:
        setting = (0, 0, height, height / 1.6)
        original_image = original_image.crop(setting)
    elif height > width:
        setting = (0, 0, width, width / 1.6)
        original_image = original_image.crop(setting)

    original_image.thumbnail(size)
    original_image.save(f'{output_path}{hash_key}.png', format='png')
    with open(f'{output_path}thumbs.json', 'r', encoding='utf-8') as thumb:
        thumbnails = load(thumb)
        thumbnails[hash_key] = f'{output_path}{hash_key}.png'
    with open(f'{output_path}thumbs.json', 'w', encoding='utf-8') as thumb:
        dump(thumbnails, thumb)

