from rocket.launch import launch
from rocket.missile import Scaffold, AppBar, Button
from rocket.widget.shape import FilledBox, String
from rocket.widget.layout import Column
from rocket.widget import Widget, color
from rocket.debug import debug


@debug
class MyOwnApp (Widget):
    def build(self):
        return Scaffold(
            app_bar=AppBar(
                child=String(
                    text='Well done'
                )
            ),
            body=Column(
                children=(
                    Button(child=FilledBox(
                        size=(100, 30)
                    )),
                )
            )
        )


launch(MyOwnApp())
