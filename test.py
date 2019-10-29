from rocket.launch import launch
from rocket.widget.shapes.circle import FilledCircle
from rocket.widget.core import Widget
from reloadr import autoreload


class Test2(Widget):
    def build(self, context):
        return Test(self)

class Test(Widget):
    def build(self, context):
        return FilledCircle(10)


class MyApp(Widget):
    def build(self, context):
        text = Test2(self)
        return text


launch(MyApp(None))
