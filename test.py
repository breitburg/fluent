from rocket.launch import launch
from rocket.widget.shape import FilledBox
from rocket.widget.layout import Overlay, Column, Row
from rocket.widget import Widget, color, align


class MyOwnApp (Widget):
    def build(self):
        return Row(
            children=(
                FilledBox(
                    size=(100, 100)
                ),
                FilledBox(
                    size=(200, 200)
                )
            ),
            spacing=0
        )


launch(MyOwnApp())
