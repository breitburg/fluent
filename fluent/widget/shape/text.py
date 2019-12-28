from fluent.render import window, manager
from fluent.render.property import Color, Weight
from fluent.widget import GenericWidget


class Text(GenericWidget):
    """A class used to represent an text

    Parameters
    ----------
    text : str
        text that will be displayed

    color : tuple, optional
        color that will be using to draw

    size : int, optional
        size of the text

    weight : str, optional
        weight of the text
    """

    def __init__(self, text, color=Color.black, size=16, weight=Weight.regular):
        self.text = text
        self.color = color
        self.weight = weight
        self.font_size = int(size * window.scale)

        self._apply_changes()
        super(Text, self).__init__(size=self.texture.size)

    def render(self, xy):
        self._apply_changes()
        window.renderer.copy(self.texture, dstrect=(xy[0], xy[1], self.texture.size[0], self.texture.size[1]))

    def _apply_changes(self):
        manager.size = self.font_size
        manager.default_font = self.weight
        manager.color = self.color

        self.texture = window.factory.from_text(self.text, fontmanager=manager)
        self.__size__ = self.texture.size
