from rocket.widget import Widget, Rectangle, Text, Overlay, Padding, Column, Row
from rocket.material import PushButton


class Alert (Widget):
    def __init__(self, title=None, subtitle=None, button=PushButton(child=Text('OK'))):
        super(Alert, self).__init__()

        self.title = title
        self.subtitle = subtitle
        self.button = button

    def build(self):
        rectangle = Padding(
                child=Column(
                    children=(self.title, self.subtitle, self.button),
                    spacing=10
                ),
                padding=20
            )

        return Overlay(
            top=rectangle,
            bottom=Rectangle(
                size=rectangle.get_size()
            )
        )

    def pressed(self, button):
        pass
