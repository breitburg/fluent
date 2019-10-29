from rocket.widget.core import Widget
from rocket.widget.shapes import FilledCircle
from rocket.launch import launch
from rocket.widget.layout import Overlay, Padding, Align
from reloadr import autoreload


@autoreload
class MyApp(Widget):
    def build(self):
        return Padding(
            child=Overlay(
                top=FilledCircle(radius=50, color=(0, 255, 0, 100)),
                bottom=FilledCircle(radius=100, color=(255, 0, 0, 255)),
                align=(Align.right, Align.center)
            ),
            value=20
        )


launch(MyApp())
