from fluent.widget.core import GenericWidget


class Overlay(GenericWidget):
    """A class used to represent an overlay

    Parameters
    ----------
    top : Widget
        top widget in the overlay

    bottom : Widget
        bottom widget in the overlay
    """

    def __init__(self, bottom, top):
        self.bottom = bottom

        self.top = top
        self.top.parent = self.bottom

        super(Overlay, self).__init__(size=self.bottom.size)

    def render(self, xy):
        for widget in [self.bottom, self.top]:
            widget.render(xy=xy)
