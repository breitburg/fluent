from fluent.core.font import default
from fluent.core.property import Color, Weight
from fluent.core.widget import RenderWidget
from fluent.core.window import window


class Text(RenderWidget):
    def __init__(self, text, font=default, color=Color(red=0, green=0, blue=0),
                 size=24, weight=Weight(string='product_sans_regular')):
        self.text = text
        self.color = color
        self.font = font
        self.weight = weight
        self.font_size = size

        self._apply_changes()
        super(Text, self).__init__(size=self.texture.size)

    def render(self, xy):
        self._apply_changes()

        window.renderer.copy(self.texture, dstrect=(xy[0], xy[1], self.texture.size[0], self.texture.size[1]))

    def _apply_changes(self):
        self.font.set_size(size=self.font_size)
        self.font.set_weight(weight=self.weight)
        self.font.set_color(color=self.color.rgba)

        self.texture = self.font.texture(text=self.text)
        self.__size__ = self.texture.size
