from fluent.widget.core import GenericWidget


class Center(GenericWidget):
    def __init__(self, child):
        self.child = child

        super(Center, self).__init__(size=(0, 0))

    def render(self, xy):
        self._size = self.parent.size

        centered = (int((self.size[0] - self.child.size[0]) / 2), int((self.size[1] - self.child.size[1]) / 2))
        self.child.render(xy=centered)
