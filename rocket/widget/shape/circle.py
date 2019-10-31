from rocket.render import filledCircleRGBA, circleRGBA, aacircleRGBA, window
from rocket.widget import GenericWidget, color


class FilledCircle(GenericWidget):
    def __init__(self, radius, color=color.white):
        self.radius = radius
        self.color = color

        super(FilledCircle, self).__init__(size=(self.radius * 2, self.radius * 2))

    def render(self, xy):
        filledCircleRGBA(
            window.renderer.sdlrenderer,
            xy[0] + self.radius, xy[1] + self.radius, self.radius,
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )


class OutlineCircle(GenericWidget):
    def __init__(self, radius, color=color.white, anti_aliasing=True):
        self.radius = radius
        self.color = color
        self.anti_aliasing = anti_aliasing

        super(OutlineCircle, self).__init__(size=(self.radius * 2, self.radius * 2))

    def render(self, xy):
        method = aacircleRGBA if self.anti_aliasing else circleRGBA
        method(
            window.renderer.sdlrenderer,
            xy[0] + self.radius, xy[1] + self.radius, self.radius,
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )
