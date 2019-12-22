from fluent.widget.core import GenericWidget
from fluent.render import align


class Align(GenericWidget):
    def __init__(self, child, align=(align.top, align.left)):
        self.child = child
        self.align = align

        super(Align, self).__init__(size=(0, 0))

    def render(self, xy):
        self._size = self.parent.size

        horizontal_padding = vertical_padding = 0

        if self.align[0] == align.bottom:
            vertical_padding = self._size[1] - self.child.size[1]
        elif self.align[0] == align.center:
            vertical_padding = self._size[1] / 2 - self.child.size[1] / 2

        if self.align[1] == align.right:
            horizontal_padding = self._size[0] - self.child.size[0]
        elif self.align[1] == align.center:
            horizontal_padding = self._size[0] / 2 - self.child.size[0] / 2

        self.child.render(xy=(int(xy[0] + horizontal_padding), int(xy[1] + vertical_padding)))


class Center(Align):
    def __init__(self, child):
        super(Center, self).__init__(child=child, align=(align.center, align.center))
