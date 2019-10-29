from rocket.widget.core import GenericWidget
from rocket.widget.layout import Align


class Overlay(GenericWidget):
    def __init__(self, bottom, top, align=(Align.top, Align.left)):
        self.bottom = bottom
        self.top = top
        self.align = align
        super(Overlay, self).__init__(size=self.bottom.size)

    def render(self, xy):
        self.bottom.render(xy=xy)
        horizontal_padding = vertical_padding = 0

        for coordinate in range(0, 2):
            if self.align[coordinate - 1] == 'bottom':
                vertical_padding = self.bottom.size[coordinate] - self.top.size[coordinate]
            elif self.align[coordinate - 1] == 'center':
                vertical_padding = self.bottom.size[coordinate] / 2 - self.top.size[coordinate] / 2

        self.top.render(xy=(int(xy[0] + horizontal_padding), int(xy[1] + vertical_padding)))
