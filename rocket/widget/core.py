from rocket.render import window
from sdl2.rect import SDL_Rect


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
        for touch in window.events:
            if SDL_Rect(xy[0], xy[1], self.size[0], self.size[1]).collidepoint(touch) and self.pressed is not None:
                print('Touched')

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
