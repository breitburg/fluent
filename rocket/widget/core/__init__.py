from rocket.render import touches
from pygame import Rect


class Widget:
    pressed = None

    def __init__(self, pressed=None):
        self.pressed = pressed

    def build(self): return NotImplemented

    def render(self, xy):
        rectangle = self.build().render(xy=xy)
        for touch in touches:
            if Rect(xy[0], xy[1], rectangle[0], rectangle[1]).collidepoint(touch) and self.pressed is not None:
                self.pressed()

        return rectangle

    def get_size(self): return self.render(xy=(-10000, -10000))


class CoreWidget (Widget):
    def build(self): return self
