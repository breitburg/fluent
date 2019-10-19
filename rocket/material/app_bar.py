from rocket.widget import Widget, Overlay, Padding, Rectangle
from rocket.display import get_size


class AppBar (Widget):
    def __init__(self, title, title_align=('center', 'left'), actions=None, color=(98, 33, 234)):
        super(AppBar, self).__init__()

        self.title = title
        self.title_align = title_align
        self.actions = actions
        self.color = color

    def build(self):
        return Overlay(
                top=Padding(
                    widget=self.title,
                    padding=30
                ),
                bottom=Rectangle(
                    size=(get_size()[0], 80),
                    color=self.color
                ),
                align=self.title_align
            )
