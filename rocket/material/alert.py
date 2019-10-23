from rocket.widget import Widget, Rectangle, Text, Overlay, Padding, Column, Row
from rocket.material import PushButton


class Alert (Widget):
    def __init__(self, title=None, subtitle=None, button=PushButton(child=Text('OK'))):
        super(Alert, self).__init__()

        self.title = title
        self.subtitle = subtitle
        self.button = button

    def build(self):
        rectangles = [rectangle.get_size() for rectangle in [self.title, self.subtitle, self.button]]

        return Overlay(
            top=Padding(
                child=Column(
                    children=(self.title, self.subtitle, self.button),
                    spacing=5
                ),
                padding=20
            ),
            bottom=Rectangle(
                size=(
                    max([rectangle[0] for rectangle in rectangles]),
                    sum([rectangle[1] for rectangle in rectangles])
                )
            )
        )

    def pressed(self, button):
        pass
