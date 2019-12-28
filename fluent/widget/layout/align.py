from fluent.widget.core import GenericWidget
from fluent.render.property import Aligner


class Align(GenericWidget):
    """A class used to represent an align

    Parameters
    ----------
    child : Widget
        child that we will align

    align : tuple, optional
        setting align properties
    """

    def __init__(self, child, align=(Aligner.top, Aligner.left)):
        self.child = child
        self.align = align

        super(Align, self).__init__(size=(0, 0))

    def render(self, xy):
        self._size = self.parent.size

        horizontal_padding = vertical_padding = 0

        if self.align[0] == Aligner.bottom:
            vertical_padding = self._size[1] - self.child.size[1]
        elif self.align[0] == Aligner.center:
            vertical_padding = self._size[1] / 2 - self.child.size[1] / 2

        if self.align[1] == Aligner.right:
            horizontal_padding = self._size[0] - self.child.size[0]
        elif self.align[1] == Aligner.center:
            horizontal_padding = self._size[0] / 2 - self.child.size[0] / 2

        self.child.render(xy=(int(xy[0] + horizontal_padding), int(xy[1] + vertical_padding)))


class Center(Align):
    """A class used to represent an center widget

    Parameters
    ----------
    child : Widget
        child that we will center
    """

    def __init__(self, child):
        super(Center, self).__init__(child=child, align=(Aligner.center, Aligner.center))
