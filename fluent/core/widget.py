from fluent.core.window import window


class Widget:
    def __init__(self, pressed: object = None):
        self._pressed = pressed
        self.parent = self

        # Instantiating build widget
        self._instantiate()

    def _instantiate(self) -> None:
        self._instance = self.build()

        # Checking if widget builds itself
        _parent = self.parent if self.__class__ == self._instance.__class__ else self
        self._instance.parent = _parent

    def build(self) -> object:
        raise NotImplementedError

    def render(self, xy) -> None:
        self._instantiate()
        self._instance.render(xy=xy)

        if self._pressed:
            render_size = self.size

            for touch in window.events:  # Calculating collisions
                if xy[0] + render_size[0] > touch[0] > xy[0] and \
                        xy[1] + render_size[1] > touch[1] > xy[1]:
                    self._pressed(self, (touch[0] - xy[0], touch[1] - xy[1]))

    @property
    def size(self):
        return self._instance.size


class GenericWidget(Widget):
    def __init__(self, size):
        super(GenericWidget, self).__init__()
        self._size = size

    def build(self) -> object:
        return self

    @property
    def size(self):
        return self._size
