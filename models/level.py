__author__ = 'denis'


class BaseLevel(object):
    """ Parent object for all level instances
    """

    def __init__(self):
        entities = []

    def initialize(self):
        pass

    def _load_resources(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class MenuLevel(BaseLevel):
    """ Menu level
    """
