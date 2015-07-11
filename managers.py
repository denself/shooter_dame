import pygame
from utils import singleton


@singleton
class InputManager(object):

    def __init__(self):
        # Mouse position related to prev pos: (dx, dy)
        self.mouse_rel = (0, 0)
        # Absolute pos on game screen: (x, y)
        self.mouse_pos = (0, 0)
        # Pressed mouse buttons: (left, middle, right)
        self.mouse_pressed = (0, 0, 0)
        # Changes of mouse buttons
        self.mouse_button_change = (0, 0, 0)
        # Is mouse on game screen: isOnScreen
        self.mouse_focused = 0

    def update(self):
        """ Update input values on each iteration """
        self.mouse_rel = pygame.mouse.get_rel()
        self.mouse_pos = pygame.mouse.get_pos()
        self.update_mouse_button()
        self.mouse_focused = pygame.mouse.get_focused()

    def update_mouse_button(self):
        new_values = pygame.mouse.get_pressed()
        old_to_new = zip(self.mouse_pressed, new_values)
        self.mouse_button_change = tuple([old ^ new for old, new in old_to_new])
        self.mouse_pressed = new_values
