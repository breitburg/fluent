from fluent.widget import Widget, align
from fluent.widget.layout import Overlay, Padding
from fluent.widget.shape import FilledBox
from fluent.render import window, color


class AppBar(Widget):
    def __init__(self, child, align=(align.center, align.left), bar_size=(window.size[0], 80)):
        self.child = child
        self.align = align
        self.bar_size = bar_size
        super(AppBar, self).__init__()

    def build(self):
        return Overlay(
            top=Padding(
                child=self.child,
                value=20
            ),
            bottom=FilledBox(
                color=color.blue,
                size=(self.bar_size[0], self.bar_size[1])
            ),
            align=self.align
        )
