import os
import settings

__author__ = 'Denis Ivanets (denself@gmail.com)'


def get_data_file(file_name):
    return os.path.join(settings.DATA_DIR, file_name)


def get_font_file(font_name):
    file_name = font_name + '.ttf'
    return os.path.join(settings.FONTS_DIR, file_name)