from fluent.material import *  # Importing library
from fluent.debug import auto_reload


@auto_reload
class MyApp(Widget):
    def build(self):
        return First()


@auto_reload
class First(Widget):
    def build(self):
        return Second()


@auto_reload
class Second(Widget):
    def build(self):
        print(self.parent)
        return FilledBox(size=(100, 20), color=color.white)


launch(target=MyApp())
