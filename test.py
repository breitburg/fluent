from rocket.widget import Widget, color, align
from rocket.widget.shapes import FilledBox
from rocket.launch import launch
from rocket.widget.layout import Overlay, Padding, align
from reloadr import autoreload


@autoreload
class MyApp(Widget):
    def build(self):
        return Padding(
            child=FilledBox(
                size=(20, 20)
            ),
            value=20
        )


launch(MyApp())
