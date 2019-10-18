from rocket.widget import Widget, Overlay, Rectangle
from rocket.display import get_size


class Page (Widget):
    def __init__(self, widget, background=(255, 255, 255)):
        super(Widget, self).__init__()

        self.widget = widget
        self.background = background

    def build(self):
        return Overlay(
            top=self.widget,
            bottom=Rectangle(
                size=(get_size()[0], get_size()[1] - 80)
            )
        )
