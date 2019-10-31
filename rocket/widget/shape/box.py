from rocket.render import boxRGBA, roundedBoxRGBA, \
    rectangleRGBA, roundedRectangleRGBA, window
from rocket.widget import GenericWidget, color


class FilledBox(GenericWidget):
    def __init__(self, size, color=color.white):
        self.color = color
        super(FilledBox, self).__init__(size=size)

    def render(self, xy):
        boxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )


class FilledRoundedBox(GenericWidget):
    def __init__(self, size, color=color.white, radius=10):
        self.color = color
        self.radius = radius
        super(FilledRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedBoxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )


class OutlineBox(GenericWidget):
    def __init__(self, size, color=color.white):
        self.color = color
        super(OutlineBox, self).__init__(size=size)

    def render(self, xy):
        rectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )


class OutlineRoundedBox(GenericWidget):
    def __init__(self, size, color=color.white, radius=10):
        self.color = color
        self.radius = radius
        super(OutlineRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedRectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )
