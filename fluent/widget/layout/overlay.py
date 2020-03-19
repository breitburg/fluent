from fluent.core.widget import RenderWidget


class Overlay(RenderWidget):
    def __init__(self, bottom, top):
        self.bottom = bottom

        self.top = top
        self.top.parent = self.bottom

        super(Overlay, self).__init__(size=self.bottom.size)

    def render(self, xy):
        for widget in [self.bottom, self.top]:
            widget.render(xy=xy)
