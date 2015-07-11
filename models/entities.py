import pygame
from managers import InputManager
from resources import ResourceManager, Texture

__author__ = 'denis'


class BaseEntity(object):
    """ Base entity, defines interface for all children """

    def update(self, *args, **kwargs):
        pass

    def draw(self, *args, **kwargs):
        pass


class BaseButtonEntity(BaseEntity):
    """ Base class for all buttons"""

    def __init__(self, top=0, left=0, width=120, height=80):
        super(BaseButtonEntity, self).__init__()
        self.geometry = pygame.Rect(top, left, width, height)
        self.inspector = InputManager()

    def update(self, *args, **kwargs):
        """ This function called from level update method.
        """
        if self.clicked():
            self.callback()

    def draw(self, surface, *args, **kwargs):
        """ This function called from level draw method.
        """
        surface.blit(self.get_surface(), self.geometry.topleft)

    def is_mouse_over(self):
        """ Checks whether mouse over
        :rtype: bool
        """
        return self.geometry.collidepoint(*self.inspector.mouse_pos)

    def is_mouse_pressed(self):
        """ Checks whether mouse pressed
        :rtype: boot
        """
        return self.is_mouse_over() and self.inspector.mouse_pressed[0]

    def get_color(self):
        """ Return button color depended on button state
        :return: Color set
        :rtype: tuple
        """
        return 25, 25, 25

    def get_surface(self):
        """ Return calculated button surface
        :rtype: pygame.Surface
        """
        color = self.get_color()
        surface = pygame.Surface(self.geometry.size)
        surface.fill(color)
        return surface

    def clicked(self):
        """ Check whether mouse was clicked on this button.
        :rtype: bool
        """
        return self.is_mouse_over() and \
            self.inspector.mouse_button_change[0] and \
            not self.inspector.mouse_pressed[0]

    def callback(self):
        """ callback function, called if mouse clicked
        """
        pass


class TestButton(BaseButtonEntity):

    def callback(self):
        print 'Clicked!'

    def get_color(self):
        """ Return button color depended on button state
        :return: Color set
        :rtype: tuple
        """
        if self.is_mouse_pressed():
            return 0xFF, 0x00, 0x00
        elif self.is_mouse_over():
            return 0xD1, 0xCD, 0xCD
        else:
            return 0xB3, 0xB6, 0xB6


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
