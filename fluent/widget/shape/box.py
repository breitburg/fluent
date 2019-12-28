from fluent.render import boxRGBA, roundedBoxRGBA, \
    rectangleRGBA, roundedRectangleRGBA, window
from fluent.render.property import Color
from fluent.widget import GenericWidget


class FilledBox(GenericWidget):
    """A class used to represent an filled box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw
    """

    def __init__(self, size, color=Color.white):
        self.color = color

        super(FilledBox, self).__init__(size=size)

    def render(self, xy):
        boxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class FilledRoundedBox(GenericWidget):
    """A class used to represent an filled rounded box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw

    radius : int, optional
        radius that will be using on corners
    """

    def __init__(self, size, color=Color.white, radius=10):
        self.color = color
        self.radius = radius

        super(FilledRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedBoxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class OutlineBox(GenericWidget):
    """A class used to represent an outline box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw outline
    """

    def __init__(self, size, color=Color.white):
        self.color = color

        super(OutlineBox, self).__init__(size=size)

    def render(self, xy):
        rectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color[0], self.color[1], self.color[2], self.color[3]
        )


class OutlineRoundedBox(GenericWidget):
    """A class used to represent an outline rounded box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw

    radius : int, optional
        radius that will be using on corners
    """

    def __init__(self, size, color=Color.white, radius=10):
        self.color = color
        self.radius = radius

        super(OutlineRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedRectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color[0], self.color[1], self.color[2], self.color[3]
        )
