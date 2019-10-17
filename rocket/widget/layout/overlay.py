from rocket.widget.core import CoreWidget


class Overlay (CoreWidget):
    def __init__(self, bottom, top, align=('top', 'left')):
        super(Overlay, self).__init__()

        self.bottom = bottom
        self.top = top
        self.align = align

    def render(self, xy):
        bottom_rectangle = self.bottom.render(xy=xy)
        top_rectangle = self.top.get_size()
        horizontal_padding = vertical_padding = 0

        if self.align[0] == 'bottom':
            vertical_padding = bottom_rectangle[1] - top_rectangle[1]
        elif self.align[0] == 'center':
            vertical_padding = bottom_rectangle[1] / 2 - top_rectangle[1] / 2

        if self.align[1] == 'right':
            horizontal_padding = bottom_rectangle[0] - top_rectangle[0]
        elif self.align[0] == 'center':
            horizontal_padding = bottom_rectangle[0] / 2 - top_rectangle[0] / 2

        self.top.render(xy=(xy[0] + horizontal_padding, xy[1] + vertical_padding))
