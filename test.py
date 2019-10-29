from rocket.widget.core import Widget
from rocket.widget.shapes import String, OutlineCircle
from rocket.launch import launch
from rocket.widget.layout import Overlay, Padding, Align
from reloadr import autoreload


@autoreload
class MyApp(Widget):
    def build(self):
        return Padding(
            child=Overlay(
                top=String('Hacking'),
                bottom=OutlineCircle(radius=100, color=(255, 255, 255, 255)),
                align=(Align.center, Align.center)
            ),
            value=20
        )


launch(MyApp())
