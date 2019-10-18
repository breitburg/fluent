from rocket.widget import Widget, Overlay, Column, Rectangle


class Scaffold (Widget):
    def __init__(self, app_bar, home, floating_action_button=None):
        super(Scaffold, self).__init__()

        self.app_bar = app_bar
        self.home = home
        self.floating_action_button = floating_action_button

    def build(self):
        return Overlay(
            top=Rectangle(size=(0, 0)) if self.floating_action_button is None else self.floating_action_button,
            bottom=Column(
                children=(
                    self.app_bar,
                    self.home
                )
            ),
            align=('bottom', 'right')
        )
