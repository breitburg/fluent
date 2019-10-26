from rocket.widget import Widget, Overlay


class Center (Widget):
    def __init__(self, child, bottom):
        super(Center, self).__init__()

        self.child = child
        self.bottom = bottom

    def build(self):
        return Overlay(
            top=self.child,
            bottom=self.bottom,
            align=('center', 'center')
        )
