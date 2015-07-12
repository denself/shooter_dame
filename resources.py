from utils import ResourceManager
import pygame
from utils.files import get_font_file


@ResourceManager.resource
class Texture(object):

    def __init__(self, name=None):
        self.data = pygame.image.load(name).convert_alpha()

    def get(self):
        return self.data

    @classmethod
    def get_key(cls, name):
        """ Generates key, used to get Font from Resource manager """
        return name


@ResourceManager.resource
class Font(pygame.font.Font):
    """ Font resource, helps to load custom font from file """

    pattern = '{}:{}'

    def __init__(self, name, size):
        """ Get font from file in settings.FONTS_DIR
        :param name: Font name
        :param size: Font size
        """
        file_name = get_font_file(name)
        pygame.font.Font.__init__(self, file_name, size)

    @classmethod
    def get_key(cls, name, size):
        """ Generates key, used to get Font from Resource manager """
        return cls.pattern.format(name, size)
