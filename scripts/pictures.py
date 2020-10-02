from PIL import Image
from json import load, dump
from os import remove
from copy import copy

from scripts.db import get_info_from_db

output_path = 'GUI\pictures\\thumbs\\'
images = {
    elem[0]: {
        'steam_path': elem[1],
        'cache_path': elem[2],
        'steam_id': elem[3],
    } for elem in get_info_from_db('get_images')
}


def scale_image(path, hashKey):
    size = (160, 100)
    original_image = Image.open(path)
    width, height = original_image.size

    if width - height > 200:
        cutter = (0, 0, height * 1.6, height)
        original_image = original_image.crop(cutter)
    elif width >= height:
        cutter = (0, 0, height, height / 1.6)
        original_image = original_image.crop(cutter)
    elif height > width:
        cutter = (0, 0, width, width / 1.6)
        original_image = original_image.crop(cutter)

    original_image.thumbnail(size)
    original_image.save(f'{output_path}{hashKey}.png', format='png')
    with open(f'{output_path}thumbs.json', 'r', encoding='utf-8') as thumb:
        thumbnails = load(thumb)
        thumbnails[hashKey] = f'{output_path}{hashKey}.png'
    with open(f'{output_path}thumbs.json', 'w', encoding='utf-8') as thumb:
        dump(thumbnails, thumb)


def get_thumbnail(hashKey):
    try:
        with open(f'{output_path}\\thumbs.json', 'r', encoding='utf-8') as thumb:
            thumbnails = load(thumb)
        return thumbnails[hashKey]
    except KeyError:
        return f'{output_path}DoesNotExists.png'


def thumbs_synchronize():
    with open(f'{output_path}thumbs.json', 'r', encoding='utf-8') as thumbs:
        thumbnails = load(thumbs)
        scan = copy(thumbnails)
    for hashKey in scan:
        if hashKey not in images:
            del thumbnails[hashKey]
            remove(f'{output_path}{hashKey}.png')
    with open(f'{output_path}thumbs.json', 'w', encoding='utf-8') as thumb:
        dump(thumbnails, thumb)
    for hashKey in images:
        if hashKey not in thumbnails:
            try:
                scale_image(images[hashKey]["cache_path"], hashKey)
            except FileNotFoundError:
                pass
            except AttributeError:
                pass
