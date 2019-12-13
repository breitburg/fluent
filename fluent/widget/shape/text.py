from fluent.render import window, manager
from fluent.widget import GenericWidget, color


class Text(GenericWidget):
    def __init__(self, text, color=color.white):
        self.text = text
        self.color = color
        self.texture = window.factory.from_text(self.text, fontmanager=manager)

        super(Text, self).__init__(size=self.texture.size)

    def render(self, xy):
        window.renderer.copy(self.texture, dstrect=(xy[0], xy[1], self.texture.size[0], self.texture.size[1]))
