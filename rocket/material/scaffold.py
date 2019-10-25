from rocket.widget import Widget, Overlay, Column, Rectangle
from rocket.display import get_size


class Scaffold (Widget):
    def __init__(self, app_bar, body, floating_action_button=None):
        super(Scaffold, self).__init__()

        self.app_bar = app_bar
        self.body = body
        self.floating_action_button = floating_action_button

    def build(self):
        return Overlay(
            top=Rectangle(size=(0, 0)) if self.floating_action_button is None else self.floating_action_button,
            bottom=Column(
                children=(
                    self.app_bar,
                    Overlay(
                        top=self.body,
                        bottom=Rectangle(
                            size=(get_size()[0], get_size()[1] - 80)
                        )
                    )
                )
            ),
            align=('bottom', 'right')
        )
