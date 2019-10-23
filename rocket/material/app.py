from rocket.widget import Widget, Overlay, Text, Rectangle
from rocket.display import get_size
from rocket.material import Alert, PushButton


class App (Widget):
    def __init__(self, home, overlay=Rectangle((-1, -1))):
        super(App, self).__init__()

        self.home = home
        self.overlay = overlay

    def build(self):
        return Overlay(
            top=self.overlay,
            bottom=self.home
        )

    def display_alert(self, title, subtitle, button):
        self.overlay = Overlay(
            top=Alert(
                title=Text(title),
                subtitle=Text(subtitle),
                button=PushButton(button)
            ),
            bottom=Rectangle(
                size=get_size(),
                color=(0, 0, 0)
            ),
            align=('center', 'center')
        )