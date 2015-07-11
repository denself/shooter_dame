__author__ = 'denis'


class BaseEntity(object):
    """
    """

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class PrinterEntity(BaseEntity):

    def __init__(self, text):
        super(self.__class__, self).__init__()
        self.text = text

    def update(self):
        pass

    def draw(self):
        print self.text
