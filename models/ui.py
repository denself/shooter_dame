import pygame
from .entities import BaseEntity
from managers import InputManager
from resources import Font, Texture
import settings

__author__ = 'Denis Ivanets (denself@gmail.com)'


class BaseUIEntity(BaseEntity):

    MARGIN_V = 10
    MARGIN_H = 10
    BORDER_WIDTH = 1
    BORDER_COLOR = 20, 20, 20
    BACKGROUND_COLOR = 0xB3, 0xB6, 0xB6, 0xFF

    def __init__(self, geometry=(0, 0, 120, 80)):
        super(BaseUIEntity, self).__init__()
        self.geometry = pygame.Rect(geometry)
        self.inspector = InputManager()

    def draw(self, surface, *args, **kwargs):
        """ This function called from level draw method.
        """
        surface.blit(self.get_surface(), self.geometry.topleft)

    def get_surface(self):
        """ Return calculated button surface
        :rtype: pygame.Surface
        """
        surface = pygame.Surface(self.geometry.size)
        surface.fill(self.BACKGROUND_COLOR)
        return surface


class BaseButtonEntity(BaseUIEntity):
    """ Base class for all buttons"""

    def __init__(self, text='', **kwargs):
        super(BaseButtonEntity, self).__init__(**kwargs)
        self._text = text
        # TODO: refactor this
        l_width = max(0, self.geometry.width - 2 * self.MARGIN_H)
        l_height = max(0, self.geometry.height - 2 * self.MARGIN_V)
        l_geometry = (self.MARGIN_H, self.MARGIN_V, l_width, l_height)
        self.text = LabelEntity(text, geometry=l_geometry, size=46)

    def update(self, *args, **kwargs):
        """ This function called from level update method.
        """
        if self.clicked():
            self._callback()
            self.callback()

    def _callback(self):
        pass

    def is_mouse_over(self):
        """ Checks whether mouse over
        :rtype: bool
        """
        return self.geometry.collidepoint(*self.inspector.mouse_pos)

    def is_mouse_pressed(self):
        """ Checks whether mouse pressed
        :rtype: bool
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
        self.text.draw(surface)
        return surface

    def clicked(self):
        """ Check whether mouse was clicked on this button.
        :rtype: bool
        """
        is_clicked = self.is_mouse_over() and \
            self.inspector.mouse_button_change[0] and \
            not self.inspector.mouse_pressed[0]
        return is_clicked

    def callback(self):
        """ callback function, called if mouse clicked
        """
        pass


class TestButton(BaseButtonEntity):

    def callback(self):
        print 'Clicked: {}'.format(self)

    def get_color(self):
        """ Return button color depended on button state
        :rtype: tuple
        """
        if self.is_mouse_pressed():
            return 0xFF, 0x00, 0x00
        elif self.is_mouse_over():
            return 0xD1, 0xCD, 0xCD
        else:
            return 0xB3, 0xB6, 0xB6


class CheckBox(BaseButtonEntity):

    MARGIN_H = 25

    def __init__(self, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)
        self.is_checked = False

    def _callback(self):
        """ Change state or checkbox
        """
        self.is_checked = not self.is_checked

    def callback(self):
        print 'Switched {}: {}'.format(self.is_checked, self)

    def get_color(self):
        """ Return button color depended on button state
        :rtype: tuple
        """
        default_color = 0xB3, 0xB6, 0xB6
        color_map = {
            (1, 1, 0): (0xDD, 0x00, 0x00),
            (1, 1, 1): (0x0D, 0x00, 0x00),
            (0, 1, 0): (0xD1, 0xCD, 0xCD),
            (0, 1, 1): (0x01, 0xCD, 0xCD),
            (0, 0, 1): (0x00, 0x00, 0x00),
        }
        key = (self.is_mouse_over(), self.is_mouse_over(), self.is_checked)
        return color_map.get(key, default_color)


class ImageEntity(BaseUIEntity):
    def __init__(self, filename, **kwargs):
        super(ImageEntity, self).__init__(**kwargs)
        self.texture = Texture(filename)

    def get_surface(self):
        return self.texture.get()


class LabelEntity(BaseUIEntity):

    FONT_NAME = settings.DEFAULT_FONT
    FONT_SIZE = 24
    BACKGROUND_COLOR = 0xB3, 0xB6, 0xB6, 0x00

    def __init__(self, text, color=(255, 255, 255),
                 size=FONT_SIZE, **kwargs):
        super(LabelEntity, self).__init__(**kwargs)
        self.inspector = InputManager()
        self.text = text
        self.color = color
        self.FONT_SIZE = size
        self._init_font()

    def draw(self, surface, *args, **kwargs):
        """ This function called from level draw method.
        """
        surface.blit(self.get_surface(), self.geometry.topleft)

    def get_surface(self):
        surface = pygame.Surface(self.geometry.size, pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        surface.fill(self.BACKGROUND_COLOR)
        surface.blit(self.font.render(self.text, 1, self.color), (0, 0))
        return surface

    def update(self):
        pass

    @property
    def font_name(self):
        return self.FONT_NAME

    @font_name.setter
    def font_name(self, value):
        if self.FONT_NAME != value:
            self.FONT_NAME = value
            self._init_font()

    @property
    def font_size(self):
        return self.FONT_SIZE

    @font_size.setter
    def font_size(self, value):
        if self.FONT_SIZE != value:
            self.FONT_SIZE = value
            self._init_font()

    def _init_font(self):
        self.font = Font(self.FONT_NAME, self.FONT_SIZE)


