import os
from pygame import Color
from pygame.rect import Rect
from models.entities import ImageEntity, LabelEntity, TestButton, CheckBox

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

    def draw(self, surface):
        for entity in self.entities:
            entity.draw(surface)


class MenuLevel(BaseLevel):
    """ Menu level
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(base_dir, "Data/test.png")
        self.entities.append(ImageEntity(image_path, Rect(0, 0, 100, 100)))
        # self.entities.append(LabelEntity(300, 100, "hello world!", "Times New Roman", 32, Color(255, 0, 0)))
        self.entities.append(TestButton('Hello', size=(300, 100, 220, 80)))
        self.entities.append(TestButton('Hello', size=(300, 200, 220, 80)))
        self.entities.append(CheckBox('Hello', size=(300, 300, 220, 80)))
