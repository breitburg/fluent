from rocket.widget.core import CoreWidget
from rocket.render import surface

from pygame import draw


class Ellipse (CoreWidget):
    def __init__(self, size, color=(255, 255, 255)):
        super(Ellipse, self).__init__()

        self.color = color
        self.size = size

    def render(self, xy):
        draw.ellipse(surface, self.color, (xy[0], xy[1], self.size[0], self.size[1]))
        return self.size
