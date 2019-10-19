from rocket import launch, material, widget


class MyApp (widget.Widget):
    hello = 0

    def build(self):
        return material.Scaffold(
            app_bar=material.AppBar(
                title=widget.Text('Material App Demo')
            ),
            body=material.Page(
                widget.Padding(
                    widget=widget.Column(
                        children=(
                            widget.Text(f'Number: {self.hello}', color=(20, 20, 20)),
                            material.PushButton('Press here', pressed=self.on_button_press)
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
