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

    def draw(self):
        for entity in self.entities:
            entity.draw()


class MenuLevel(BaseLevel):
    """ Menu level
    """

    def __init__(self):
        super(self.__class__, self).__init__()
