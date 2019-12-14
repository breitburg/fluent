from fluent.widget.core import GenericWidget
from fluent.render import align


class Overlay(GenericWidget):
    def __init__(self, bottom, top, align=(align.top, align.left)):
        self.bottom = bottom
        self.top = top
        self.align = align

        super(Overlay, self).__init__(size=self.bottom.size)

    def render(self, xy):
        self.bottom.render(xy=xy)
        horizontal_padding = vertical_padding = 0

        if self.align[0] == 'bottom':
            vertical_padding = self.bottom.size[1] - self.top.size[1]
        elif self.align[0] == 'center':
            vertical_padding = self.bottom.size[1] / 2 - self.top.size[1] / 2

        if self.align[1] == 'right':
            horizontal_padding = self.bottom.size[0] - self.top.size[0]
        elif self.align[1] == 'center':
            horizontal_padding = self.bottom.size[0] / 2 - self.top.size[0] / 2

        self.top.render(xy=(int(xy[0] + horizontal_padding), int(xy[1] + vertical_padding)))
