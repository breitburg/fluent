from fluent.render import window


class Widget:
    def __init__(self, pressed=None):
        self._pressed = pressed
        self._update_instance()

    def build(self):
        return NotImplemented

    def _update_instance(self):
        self._instance = self.build()

    def render(self, xy):
        self._update_instance()
        self._instance.render(xy=xy)

        widget_size = self.size
        for touch in window.events:
            if xy[0] + widget_size[0] > touch[0] > xy[0] and \
                    xy[1] + widget_size[1] > touch[1] > xy[1] and \
                    self._pressed:
                self._pressed(self)

    @property
    def size(self):
        return self._instance.size


class GenericWidget(Widget):
    def __init__(self, size):
        self._size = size
        super(GenericWidget, self).__init__()

    def build(self):
        return self

    @property
    def size(self):
        return self._size
