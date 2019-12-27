from fluent.essential import *  # Importing library


class MyOwnWidget(Widget):
    def build(self):
        return Text(text='Hello, world', color=color.white)


launch(target=MyOwnWidget())
