from rocket.widget.core import CoreWidget

from rocket.render import font_regular, font_bold, surface


class Text (CoreWidget):
    def __init__(self, text, font='regular', color=(255, 255, 255), antialiased=True):
        super(Text, self).__init__()

        self.antialiased = antialiased
        self.font = font_regular if font == 'regular' else font_bold
        self.text = text
        self.color = color

    def render(self, xy):
        text = font_regular.render(self.text, self.antialiased, self.color)
        surface.blit(text, xy)

        rectangle = text.get_rect()
        return rectangle.width, rectangle.height
