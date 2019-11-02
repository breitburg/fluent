from rocket.launch import launch
from rocket.missile import Scaffold, AppBar
from rocket.widget.shape import FilledBox, String
from rocket.widget.layout import Column
from rocket.widget import Widget, color
from reloadr import autoreload


@autoreload
class MyOwnApp (Widget):
    def build(self):
        return Scaffold(
            app_bar=AppBar(
                child=String(
                    text='Hello'
                )
            ),
            body=Column(
                children=(
                    FilledBox(size=(100, 100), color=color.red),
                )
            )
        )


launch(MyOwnApp())
