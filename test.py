from rocket.launch import launch
from rocket.widget.shapes import FilledBox
from rocket.widget.core import Widget
from reloadr import autoreload


class Test2(Widget):
    def build(self, context):
        return Test(self)


class Test(Widget):
    def build(self, context):
        return FilledBox(size=(100, 100))


class MyApp(Widget):
    def build(self, context):
        text = Test2(self)
        return text


launch(MyApp)
