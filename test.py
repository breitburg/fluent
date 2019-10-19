from rocket import launch, material, widget


class MyApp (widget.Widget):
    hello = 0

    def build(self):
        return material.Scaffold(
            app_bar=material.AppBar(
                title=widget.Text('Hello, world')
            ),
            body=material.Page(
                widget.Padding(
                    widget=widget.Row(
                        children=(
                            widget.Rectangle(size=(self.hello, self.hello), color=(0, 0, 0)),
                            material.PushButton('Нажмите сюда', pressed=self.on_button_press)
                        ),
                        spacing=20
                    ),
                    padding=20
                )
            )
        )

    def on_button_press(self):
        self.hello += 1


launch(MyApp())