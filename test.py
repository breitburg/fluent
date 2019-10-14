import rocket
import random


class MyOwnCoolApp (rocket.widget.Widget):
    def build(self, context=None):
        return rocket.widget.Row(children=(
            rocket.widget.Rectangle(size=(random.randint(0, 200), random.randint(0, 200)), color=(255, 0, 0)),
            rocket.widget.Rectangle(size=(200, 200), color=(0, 255, 0)),
            rocket.widget.Rectangle(size=(200, 200), color=(0, 0, 255)),
            rocket.widget.Text('So cool!')
        ), spacing=20)


if __name__ == '__main__':
    rocket.run_app(MyOwnCoolApp())
