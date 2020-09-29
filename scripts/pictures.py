from requests import get
from os import mkdir, listdir
from scripts.db import write_data_into_db, get_info_from_db
from scripts.utils import paradox_folder

images = {
    elem[0]: {
        'steam_path': elem[1],
        'cache_path': elem[2],
        'steam_id': elem[3],
    } for elem in get_info_from_db('get_images')
}


def download_image(url, file_name, steam_id):
    response = get(url)
    if '.' in file_name:
        path = f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{steam_id}\\{file_name}'
    else:
        path = f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{steam_id}\\{file_name}'  # TODO
        write_data_into_db('write_new_image_path', {'image_path': path,
                                                    'steam_id': steam_id})
    with open(path, 'wb') as file:
        file.write(response.content)
    return path


def get_images(mod_id):
    image_pth = images[mod_id]
    if not image_pth['cache_path'] and not image_pth['steam_path']:
        return None
    if not image_pth['cache_path'] and image_pth['steam_path']:
        mkdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
        image_pth['cache_path'] = download_image(image_pth['steam_path'],
                                                 image_pth['steam_path'].split('/')[-2].lower(),
                                                 image_pth['steam_id'])
        return image_pth['cache_path']
    try:
        directory = listdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
        if directory:
            return image_pth['cache_path']
        image_pth['cache_path'] = download_image(image_pth['steam_path'],
                                                 image_pth['cache_path'].split('\\')[-1],
                                                 image_pth['steam_id'])
        return image_pth['cache_path']
    except FileNotFoundError:
        mkdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
        image_pth['cache_path'] = download_image(image_pth['steam_path'],
                                                 image_pth['cache_path'].split('\\')[-1],
                                                 image_pth['steam_id'])
        return image_pth['cache_path']
