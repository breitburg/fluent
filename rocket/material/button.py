from rocket.widget import Widget, Overlay, Padding, Text, Rectangle, Ellipse


class PushButton (Widget):
    def __init__(self, child, color=(98, 33, 234), padding=20, pressed=lambda: None):
        super(PushButton, self).__init__(pressed=pressed)

        self.color = color
        self.top_text = Padding(
            child=child,
            padding=padding
        )

    def build(self):
        return Overlay(
            top=self.top_text,
            bottom=Rectangle(size=self.top_text.get_size(), color=self.color)
        )


class FloatingActionButton (Widget):
    def __init__(self, color=(98, 33, 234), pressed=lambda: None):
        super(FloatingActionButton, self).__init__(pressed=pressed)
        self.color = color

    def build(self):
        return Padding(
            child=Ellipse(size=(80, 80), color=self.color),
            padding=20
        )
