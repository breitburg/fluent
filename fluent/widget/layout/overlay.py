from fluent.widget.core import GenericWidget
from fluent.render import align


class Overlay(GenericWidget):
    def __init__(self, bottom, top):
        self.bottom = bottom

        self.top = top
        self.top.parent = self.bottom

        super(Overlay, self).__init__(size=self.bottom.size)

    def render(self, xy):
        for widget in [self.bottom, self.top]:
            widget.render(xy=xy)
