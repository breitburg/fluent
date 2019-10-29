from rocket.render import boxRGBA, roundedBoxRGBA, \
    rectangleRGBA, roundedRectangleRGBA, window
from rocket.widget.core import GenericWidget


class FilledBox(GenericWidget):
    def __init__(self, size, color=(255, 255, 255, 255)):
        self.size = size
        self.color = color

        super(FilledBox, self).__init__()

    def render(self, xy):
        boxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class FilledRoundedBox(GenericWidget):
    def __init__(self, size, color=(255, 255, 255, 255), radius=10):
        self.size = size
        self.color = color
        self.radius = radius

        super(FilledRoundedBox, self).__init__()

    def render(self, xy):
        roundedBoxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class OutlineBox(GenericWidget):
    def __init__(self, size, color=(255, 255, 255, 255)):
        self.size = size
        self.color = color

        super(OutlineBox, self).__init__()

    def render(self, xy):
        rectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class OutlineRoundedBox(GenericWidget):
    def __init__(self, size, color=(255, 255, 255, 255), radius=10):
        self.size = size
        self.color = color
        self.radius = radius

        super(OutlineRoundedBox, self).__init__()

    def render(self, xy):
        roundedRectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color[0], self.color[1], self.color[2], self.color[3]
        )
