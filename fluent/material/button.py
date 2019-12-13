from fluent.widget import Widget, align
from fluent.render import color
from fluent.widget.shape import FilledRoundedBox
from fluent.widget.layout import Overlay


class Button(Widget):
    def __init__(self, child, color=color.blue, pressed=None):
        self.child = child
        self.color = color
        super(Button, self).__init__(pressed=pressed)

    def build(self):
        return Overlay(
            top=self.child,
            bottom=FilledRoundedBox(
                size=(self.child.size[0] + 30, self.child.size[1] + 30),
                color=self.color
            ),
            align=(align.center, align.center)
        )
