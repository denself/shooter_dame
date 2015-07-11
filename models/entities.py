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
