from fluent.material import *
from fluent.debug import auto_reload


@auto_reload
class MyApp(Widget):
    text = 'Hello'

    def build(self):
        return Scaffold(
            app_bar=AppBar(
                child=Text('Hello, world', color=color.white),
                color=color.red
            ),
            body=Padding(
                child=Row(
                    children=(
                        Button(
                            child=Text('Press here', color=color.white),
                            color=color.black,
                            pressed=self.on_button_pressed
                        ),
                        Text(self.text)
                    )
                ),
                value=10
            )
        )

    def on_button_pressed(self, button):
        self.text += ' world'


launch(MyApp())
