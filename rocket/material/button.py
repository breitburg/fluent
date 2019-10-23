from rocket.widget import Widget, Overlay, Padding, Text, Rectangle, Ellipse


class PushButton (Widget):
    def __init__(self, child, color=(98, 33, 234), padding=20, pressed=lambda button: None):
        super(PushButton, self).__init__(pressed=pressed)

        self.color = color
        self.child = Padding(
            child=child,
            padding=padding
        )

    def build(self):
        return Overlay(
            top=self.child,
            bottom=Rectangle(size=self.child.get_size(), color=self.color)
        )


class FloatingActionButton (Widget):
    def __init__(self, child, color=(98, 33, 234), pressed=lambda: None):
        super(FloatingActionButton, self).__init__(pressed=pressed)

        self.color = color
        self.child = child

    def build(self):
        return Overlay(
            top=self.child,
            bottom=Padding(
                child=Ellipse(size=(80, 80), color=self.color),
                padding=20
            ),
            align=('center', 'center')
        )
