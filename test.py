from fluent.material import *
from fluent.debug import auto_reload


@auto_reload
class MyApp(Widget):
    def build(self):
        return Scaffold(
            app_bar=AppBar(
                child=Text('Hello, world', color=color.white)
            ),
            body=Padding(
                child=Text('Welcome'),
                value=10
            )
        )

    def on_button_pressed(self, button):
        self.private_text += ' hello'


launch(MyApp())
