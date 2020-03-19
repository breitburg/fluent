from fluent.core.window import window


class Widget:
    def __init__(self, pressed=None):
        self._pressed = pressed

        # Instantiating build widget
        self._instantiate()

    def _instantiate(self) -> None:
        self._instance = self.build()  # Setting up build widget

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


class RenderWidget(Widget):
    def __init__(self, size):
        super(RenderWidget, self).__init__()
        self._size = size

    def build(self) -> object:
        return self

    @property
    def size(self):
        return self._size
