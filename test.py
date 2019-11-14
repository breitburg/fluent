from rocket.launch import launch
from rocket.widget import Widget, color
from rocket.widget.layout import Row, Padding
from rocket.widget.shape import FilledBox


class MyWid(Widget):
    def build(self):
        return Padding(
            child=Row(
                children=(
                    FilledBox(
                        size=(10, 10),
                        color=color.red
                    ),
                    FilledBox(
                        size=(10, 10),
                        color=color.green
                    ),
                    FilledBox(
                        size=(10, 10),
                        color=color.blue
                    )
                ),
                spacing=20
            ),
            value=20
        )


launch(
    MyWid()
)
