from rocket.widget.core import CoreWidget

from rocket.render import font, surface


class Text (CoreWidget):
    def __init__(self, text, font=font, color=(255, 255, 255), antialiased=True):
        super(Text, self).__init__()

        self.antialiased = antialiased
        self.font = font
        self.text = text
        self.color = color

    def render(self, xy):
        text = font.render(self.text, self.antialiased, self.color)
        surface.blit(text, xy)

        rectangle = text.get_rect()
        return rectangle.width, rectangle.height
