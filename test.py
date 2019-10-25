from rocket.widget import *
from rocket.material import *
from rocket import launch, auto_reload

@auto_reload
class MyApp (Widget):
    material_app = App(None)

    def build(self):
        self.material_app.home = Scaffold(
            app_bar=AppBar(
                child=Text('Hi')
            ),
            body=Padding(
                child=PushButton(
                    child=Text('Press here'),
                    pressed=self.on_display_alert
                ),
                padding=20
            )
        )
        return self.material_app

    def on_display_alert(self, button):
        self.material_app.display_alert('a', 'aaa', 'a')


launch(MyApp())
