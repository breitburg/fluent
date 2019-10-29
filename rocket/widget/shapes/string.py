from rocket.render import stringRGBA, window
from rocket.widget.core import GenericWidget


class String(GenericWidget):
    def __init__(self, text, color=(255, 255, 255, 255)):
        self.text = text
        self.color = color
        # TODO: Add text size calculation

        super(String, self).__init__(size=(0, 0))

    def render(self, xy):
        stringRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], bytes(self.text, 'utf-8'),
            self.color[0], self.color[1], self.color[2], self.color[3]
        )
