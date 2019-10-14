import rocket

class MyOwnCoolApp (rocket.widget.Widget):
    def build(self, context=None):
        return rocket.widget.Row((
            rocket.widget.Rectangle(size=(200, 200), color=(255, 0, 0)),
            rocket.widget.Rectangle(size=(200, 200), color=(0, 255, 0)),
            rocket.widget.Rectangle(size=(200, 200), color=(0, 0, 255)),
            rocket.widget.Text('Супер!!!!!!!!!!!!!!!')
        ), spacing=20)

rocket.run_app(MyOwnCoolApp())