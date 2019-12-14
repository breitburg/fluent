from fluent.material import *
from fluent.debug import auto_reload


@auto_reload
class Pupkin(Widget):
    user_number = 0

    def build(self):
        return Scaffold(
            app_bar=AppBar(
                child=Text('Counter', color=color.white, size=30)
            ),
            body=Padding(
                child=Column(
                    children=(
                        Text(f'Your number: {self.user_number}', weight=weight.bold),
                        Row(
                            children=(
                                Button(
                                    child=Text('<<', color=color.green),
                                    color=color.black, pressed=self.on_left_click

                                ),
                                Button(
                                    child=Text('>>', color=color.green),
                                    color=color.black, pressed=self.on_right_click
                                )
                            )
                        )
                    )
                ),
                value=10
            )
        )

    def on_left_click(self, widget):
        self.user_number -= 1

    def on_right_click(self, widget):
        self.user_number += 1


launch(target=Pupkin())
