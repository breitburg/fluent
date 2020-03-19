from sdl2.sdlgfx import filledCircleRGBA, circleRGBA, aacircleRGBA

from fluent.core.property import Color
from fluent.core.widget import RenderWidget
from fluent.core.window import window


class FilledCircle(RenderWidget):
    def __init__(self, radius, color=Color(red=255, green=255, blue=255)):
        self.radius = radius
        self.color = color

        super(FilledCircle, self).__init__(size=(self.radius * 2, self.radius * 2))

    def render(self, xy):
        filledCircleRGBA(
            window.renderer.sdlrenderer,
            xy[0] + self.radius, xy[1] + self.radius, self.radius,
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )


class OutlineCircle(RenderWidget):
    def __init__(self, radius, color=Color(red=255, green=255, blue=255), anti_aliasing=True):
        self.radius = radius
        self.color = color
        self.anti_aliasing = anti_aliasing

        super(OutlineCircle, self).__init__(size=(self.radius * 2, self.radius * 2))

    def render(self, xy):
        method = aacircleRGBA if self.anti_aliasing else circleRGBA
        method(
            window.renderer.sdlrenderer,
            xy[0] + self.radius, xy[1] + self.radius, self.radius,
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )
