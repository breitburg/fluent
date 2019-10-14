import rocket

class MyApp (rocket.widget.Widget):
    def build(self, context=None):
        return rocket.widget.VerticalStack((
            rocket.widget.Text('This'),
            rocket.widget.Text('is'),
            rocket.widget.Text('example'),
            rocket.widget.HorizontalStack((
                rocket.widget.Rectangle(
                    (100, 100), color=(255, 0, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 255, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 0, 255)
                )
            ), spacing=0)
        ), spacing=20)

rocket.run_app(MyApp())