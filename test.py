import rocket


class MyApp (rocket.widget.Widget):
    padding = 0

    def build(self, context=None):
        self.padding += 1
        return rocket.layout.Column(children=(
            rocket.widget.Text('This'),
            rocket.widget.Text('is'),
            rocket.widget.Text('Rocket'),
            rocket.layout.Row(children=(
                rocket.widget.Rectangle(
                    (100, 100), color=(255, 0, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 255, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 0, 255)
                )
            ), spacing=self.padding)
        ), spacing=20)


if __name__ == '__main__':
    rocket.run_app(MyApp())
