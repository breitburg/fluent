from rocket.render import boxRGBA, window
from rocket.widget.core import GenericWidget


class Box(GenericWidget):
    def __init__(self, size=(100, 100), color=(255, 255, 255, 255)):
        self.size = size
        self.color = color

        super(Box, self).__init__()

    def render(self, xy):
        boxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color[0], self.color[1], self.color[2], self.color[3]
        )
