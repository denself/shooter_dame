import json
import os
import pygame
from models.entities import BaseEntity
from resources import Texture
import settings

__author__ = 'Denis Ivanets (denself@gmail.com)'

class Frame(object):
    geometry = (0, 0, 50, 50)
    resource_key = ''

    def __init__(self, r_key, geometry):
        self.resource_key = r_key
        self.geometry = geometry


class Sprite(BaseEntity):

    descriptor = {}
    resources = {}
    geometry = None
    angle = 0
    states = {}
    frame_len = 0
    status = 'regular'

    def __init__(self, name, geometry=(0, 0, 60, 60)):
        super(BaseEntity, self).__init__()
        self.frame_num = 0
        self.init_descriptor(name)
        self.geometry = pygame.Rect(geometry)

    def init_descriptor(self, name):
        path = os.path.join(settings.SPRITES_DIR, '{}.json'.format(name))
        with open(path, 'r') as f:
            context = f.read()
            self.descriptor = json.loads(context)
        self.angle = self.descriptor.get('angle', 0)
        for key, item in self.descriptor.get('resources', {}).items():
            path = os.path.join(settings.RESOURCES_DIR, item)
            self.resources[key] = Texture(path)

        for state, shots in self.descriptor.get('states', {}).items():
            res = []
            for resource, num, coordinates in shots:
                frame = Frame(resource, pygame.Rect(coordinates))
                for i in range(num):
                    res.append(frame)
            self.states[state] = res

    def draw(self, surface, *args, **kwargs):
        s, crop_params = self.get_surface()
        surface.blit(s, self.geometry.topleft, crop_params)

    def update(self, *args, **kwargs):
        self.frame_num = (self.frame_num + 1) % len(self.states[self.status])

    def get_surface(self):

        frame = self.states[self.status][self.frame_num]

        return self.resources[frame.resource_key].get(), frame.geometry
