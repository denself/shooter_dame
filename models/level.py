from pygame.rect import Rect
from models.ui import ImageEntity, LabelEntity, TestButton, CheckBox
from utils.files import get_data_file

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
        image_path = get_data_file('back.jpg')
        self.entities.append(ImageEntity(image_path, geometry=Rect(0, 0, 100, 100)))
        self.entities.append(TestButton('Button 1', geometry=(300, 100, 220, 80)))
        self.entities.append(LabelEntity('Hello', geometry=(300, 200, 220, 80)))
        self.entities.append(CheckBox('Check box', geometry=(300, 300, 220, 80)))
