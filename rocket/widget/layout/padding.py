from rocket.widget.core import CoreWidget


class Padding (CoreWidget):
    def __init__(self, child, padding):
        super(Padding, self).__init__()

        self.padding = padding
        self.child = child

    def render(self, xy):
        rectangle = self.child.render(xy=(
            self.padding + xy[0],
            self.padding + xy[1]
        ))

        return rectangle[0] + self.padding * 2, rectangle[1] + self.padding * 2
