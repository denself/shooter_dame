from pygame.rect import Rect
from models.entities import ImageEntity

__author__ = 'denis'


class BaseLevel(object):
    """ Parent object for all level instances
    """

    def __init__(self):
        self.entities = []

    def initialize(self):
        pass

    def _load_resources(self):
        pass

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)


class MenuLevel(BaseLevel):
    """ Menu level
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.entities.append(ImageEntity("Data\\test.png", Rect(0, 0, 100, 100)))
