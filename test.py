from rocket import launch, material, widget


class MyApp (widget.Widget):
    def build(self):
        return material.PushButton('Hello world')


launch(MyApp())
