from rocket.launch import launch
from rocket.widget.shapes.string import String
from rocket.widget.core import Widget
from reloadr import autoreload


@autoreload
class Test(Widget):
    def build(self):
        return String('Hack a thone')


class MyApp(Widget):
    def build(self):
        return Test()


launch(MyApp())
