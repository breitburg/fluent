class Widget:
    def __init__(self):
        pass

    def build(self, context=None): return NotImplemented

    def render(self, xy):
        return self.build().render(xy=xy)


class CoreWidget (Widget):
    def build(self, context=None): return self
