from fluent.essential import *
from fluent.debug import auto_reload
from fluentmd import Button

@auto_reload
class App(Widget):
    def build(self):
        return Button(
            child=Text('Click me', color=Color.white),
            color=Color.blue
        )


launch(
    target=App()
)
