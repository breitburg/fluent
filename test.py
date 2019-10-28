from rocket.launch import launch
from rocket.widget.shapes import Box
from rocket.widget.core import Widget
from reloadr import autoreload

@autoreload
class Test(Widget):
    def build(self):
        return Box((100, 200))


class MyApp(Widget):
    def build(self):
        return Test()


launch(MyApp())
