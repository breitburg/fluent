class Widget:
    def __init__(self, pressed=None):
        self.__pressed__ = pressed
        self.__update_instance__()

    def build(self):
        return NotImplemented

    def __update_instance__(self):
        self.__instance__ = self.build()

    def render(self, xy):
        self.__update_instance__()
        self.__instance__.render(xy=xy)

    @property
    def size(self):
        return self.__instance__.size


class GenericWidget(Widget):
    def __init__(self, size):
        self.__size__ = size
        super(GenericWidget, self).__init__()

    def build(self):
        return self

    @property
    def size(self):
        return self.__size__
