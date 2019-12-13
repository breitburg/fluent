from fluent.widget.core import GenericWidget


class Padding(GenericWidget):
    def __init__(self, child, value):
        self.value = value
        self.child = child

        super(Padding, self).__init__(
            size=(self.child.size[0] + self.value * 2, self.child.size[1] + self.value * 2)
        )

    def render(self, xy):
        self.child.render(xy=(
            self.value + xy[0],
            self.value + xy[1]
        ))
