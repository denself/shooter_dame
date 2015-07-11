import pygame
from resources import ResourceManager, Texture

__author__ = 'denis'


class BaseEntity(object):
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


class PrinterEntity(BaseEntity):
    def __init__(self, text):
        super(self.__class__, self).__init__()
        self.text = text

    def update(self):
        pass

    def draw(self, surface):
        print self.text


class ImageEntity(BaseEntity):
    def __init__(self, filename, geometry):
        super(ImageEntity, self).__init__()
        self.texture = ResourceManager().get_resource(Texture, filename)
        self.geometry = geometry

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.texture.get(), self.geometry)


class LabelEntity(BaseEntity):
    def __init__(self, pos_x, pos_y, text, font_name, size, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = text
        self.font = pygame.font.SysFont(font_name, size)
        self.color = color

    def draw(self, screen):
        rendered_text = self.font.render(self.text, 0, self.color)
        screen.blit(rendered_text, (self.pos_x, self.pos_y))

    def update(self):
        pass
