from fluent.widget import Widget
from fluent.widget.layout import Column, Overlay
from fluent.widget.shape import FilledBox
from fluent.render import window, color


class Scaffold(Widget):
    def __init__(self, app_bar, body):
        self.app_bar = app_bar
        self.body = body
        
        super(Scaffold, self).__init__()

    def build(self):
        return Column(
            children=(
                self.app_bar,
                Overlay(
                    top=self.body,
                    bottom=FilledBox(
                        size=(window.size[0], window.size[1] - self.app_bar.size[1]),
                        color=color.white
                    )
                )
            ),
            spacing=0
        )
