from fluent.material import *  # Importing library

class NewButton(Widget):
    def build(self):
        return FilledBox(size=(100, 100), color=color.white)

class App(Widget):
    def build(self):
        return NewButton()

launch(
    target=App()
)