class Widget:
    def __init__(self):
        pass

    def build(self):
        return NotImplemented

    def render(self, xy):
        self.build().render(xy=xy)


class GenericWidget(Widget):
    def build(self):
        return self
