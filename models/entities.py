__author__ = 'denis'


class BaseEntity(object):
    """ Base entity, defines interface for all children """

    def update(self, *args, **kwargs):
        pass

    def draw(self, *args, **kwargs):
        pass


