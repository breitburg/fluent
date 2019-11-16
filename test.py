from fluent.material import *
from fluent.debug import auto_reload


@auto_reload
class MyApp(Widget):
    private_text = 'Hello'

    def build(self):
        return Button(
            child=Text(
                text=self.private_text
            ),
            pressed=self.on_button_pressed
        )

    def on_button_pressed(self, button):
        self.private_text += ' hello'


launch(MyApp())
