class Widget:
    def __init__(self):
        pass

    def build(self): return NotImplemented

    def render(self, xy): return self.build().render(xy=xy)

    def get_size(self): return self.render(xy=(-10000, -10000))


class CoreWidget (Widget):
    def build(self): return self
