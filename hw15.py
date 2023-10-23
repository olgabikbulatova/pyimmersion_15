# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import logging
from collections import namedtuple

FORMAT = '{levelname} - {msg}'
logging.basicConfig(filename='mylog.log', filemode='w', encoding='utf-8', style='{', format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)


DirTree = namedtuple('DirTree', ['name', 'extension', 'parent_fold'])


def dirtree_info(path: str = os.getcwd()):
    print(path)
    for files in os.walk(path):
        for catalog in files[1]:
            catalog = DirTree(catalog.split('.')[0], True, files[0])
            logger.info(f'найден каталог: {catalog.name}, флаг каталога {catalog.extension} родительский каталог: {catalog.parent_fold}')
        for file in files[2]:
            file = DirTree(file.split('.')[0], file.split('.')[1] if '.' in file else None, files[0])
            logger.info(f'найден файл "{file.name}", разрешение файла  "{file.extension}" родительский каталог: {file.parent_fold}')


if __name__ == '__main__':
    dirtree_info()





