from rocket.material import *


@auto_reload
class MyApp (Widget):
    text_color = (0, 0, 0)

    def build(self):
        return Column(
            children=(
                PushButton(
                    child=Text('Press here'),
                    pressed=self.set_text_color
                ),
                Text('Hahahah', color=self.text_color),
            )
        )

    def set_text_color(self, button):
        self.text_color = (255, 255, 255)

launch(MyApp())
