from os.path import join

from sdl2.ext import FontManager

from fluent.core.property import Weight, Color
from fluent.core.window import window

path = __file__.replace('/core/font.py', '/assets/')


class Font:
    def __init__(self, paths):
        self._manager = FontManager(font_path=join(path, paths.pop(0)), size=14)

        for _font in paths:
            self._manager.add(font_path=join(path, _font), size=14)

    def set_weight(self, weight: Weight) -> None:
        self._manager.default_font = weight.string

    @property
    def weight(self) -> Weight:
        return Weight(string=self._manager.default_font)

    def set_size(self, size: int) -> None:
        self._manager.size = size

    @property
    def size(self) -> int:
        return self._manager.size

    def set_color(self, color: Color) -> None:
        self._manager.color = color

    @property
    def color(self) -> Color:
        manager_color = self._manager.color.__copy__()

        return Color(
            red=manager_color[0],
            green=manager_color[1],
            blue=manager_color[2],
            alpha=manager_color[3]
        )

    def texture(self, text: str):
        texture = window.factory.from_text(text=text, fontmanager=self._manager)
        return texture


default = Font(['product_sans_regular.ttf', 'product_sans_bold.ttf'])
