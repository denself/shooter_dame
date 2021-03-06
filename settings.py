import os

__author__ = 'Denis Ivanets (denself@gmail.com)'


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'Data')
FONTS_DIR = os.path.join(DATA_DIR, 'fonts')
SPRITES_DIR = os.path.join(DATA_DIR, 'sprites')
RESOURCES_DIR = os.path.join(SPRITES_DIR, 'resources')

DEFAULT_FONT = 'd_day_stencil'
