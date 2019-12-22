from fluent.material import *  # Importing library


class App(Widget):
    def build(self):
        print(self.parent.size)
        return Center(
            child=FilledBox(size=(100, 100), color=color.white)
        )


launch(
    target=App()
)
