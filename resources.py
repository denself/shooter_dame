import sys
import gc
from utils import singleton
import pygame

class Texture(object):
    def __init__(self, name=None, data=None):
        self.data = pygame.image.load(name).convert_alpha()

    def get(self):
        return self.data

    def __set__(self, instance, value):
        raise SyntaxError('You can not set texture')

@singleton
class ResourceManager:
    def __init__(self):
        self.resource_map = {}

    def get_resource(self, typename, name):
        res = self.resource_map.get(name)
        if res is None:
            res = typename(name)
            self.resource_map[name] = res
        return res

    def free_unused_resources(self):
        for key, value in self.resource_map.items():
            if sys.getrefcount(value) < 5:
                self.resource_map.pop(key)
                print gc.get_referrers(value)
