from fluent.render import window
from logging import debug


class Widget:
    """A class used to represent an Widget

    A widget is any graphic element of an application. A widget consists of other widgets.

    Parameters
    ----------
    pressed : method, optional
        the function that will be called when touching/clicking on the widget.

    Attributes
    ----------
    size : tuple
        the current widget size

    parent : Widget
        the parent widget of self

    Methods
    -------
    build() : Widget
        that function will return a self-representing widget
    """

    def __init__(self, pressed=None):
        self._pressed = pressed  # On widget pressed function bindings
        self.parent = self  # Adding dummy parent property

    def build(self):  # Method that will return a widget
        return NotImplemented

    def render(self, xy):
        _instance = self.build()  # Creating the build instance
        _instance.parent = self  # Setting parent to the builded instance
        _instance.render(xy=xy)  # Rendering instance
        self._size = _instance.size  # Setting self size

        for touch in window.events:  # Calculating collisions
            if xy[0] + self._size[0] > touch[0] > xy[0] and \
                    xy[1] + self._size[1] > touch[1] > xy[1] and \
                    self._pressed:  # If pressed property contains any binding
                self._pressed(self)  # Calling it with self argument

    @property
    def size(self):  # Property that contains build instance size
        return self._size


class GenericWidget(Widget):
    """A class used to represent an GenericWidget

    The Generic widget differs from the usual one in that it does not consist of other widgets,
    but has a render function that should render it on the screen.
    Also, the difference is that the generic widget, when creating, store its size.

    Parameters
    ----------
    size : tuple, optional
        the widget size

    Attributes
    ----------
    size : tuple
        the current widget size

    Methods
    -------
    render(xy)
        that function will render widget on the screen
    """

    def __init__(self, size):
        self._size = [int(point * window.scale) for point in size]  # Setting widget size
        debug(msg=f'{self} -> {self._size}')
        super(GenericWidget, self).__init__()

    def build(self):
        return self  # Returning self for rendering

    @property
    def size(self): return self._size
