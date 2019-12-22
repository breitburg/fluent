from fluent.render import window


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

    def _update_instance(self):
        self._instance = self.build()  # Creating the build instance
        self._instance.parent = self  # Setting parent to the builded instance

    def render(self, xy):
        self._update_instance()  # Updating instance
        self._instance.render(xy=xy)  # Rendering instance

        size = self.size  # Getting widget size
        for touch in window.events:  # Calculating collisions
            if xy[0] + size[0] > touch[0] > xy[0] and \
                    xy[1] + size[1] > touch[1] > xy[1] and \
                    self._pressed:  # If pressed property contains any binding
                self._pressed(self)  # Calling it with self argument

    @property
    def size(self):  # Property that contains build instance size
        return self._instance.size


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
        self._size = size  # Setting widget size

        super(GenericWidget, self).__init__()

    def build(self):
        return self  # Returning self for rendering

    @property
    def size(self):
        return self._size
