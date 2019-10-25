from rocket.widget.core import CoreWidget


class Spacer (CoreWidget):
    def __init__(self, size):
        super(Spacer, self).__init__()

        self.size = size

    def render(self, xy):
        return self.size
