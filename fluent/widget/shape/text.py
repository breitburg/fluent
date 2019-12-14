from fluent.render import window, manager, color
from fluent.render.font import weight
from fluent.widget import GenericWidget


class Text(GenericWidget):
    def __init__(self, text, color=color.black, size=16, weight=weight.regular):
        self.text = text
        self.color = color
        self.weight = weight
        self.font_size = size
        self.texture = window.factory.from_text(self.text, fontmanager=manager)

        super(Text, self).__init__(size=self.texture.size)

    def render(self, xy):
        manager.size = self.font_size
        manager.default_font = self.weight
        manager.color = self.color

        self.texture = window.factory.from_text(self.text, fontmanager=manager)
        window.renderer.copy(self.texture, dstrect=(xy[0], xy[1], self.texture.size[0], self.texture.size[1]))
