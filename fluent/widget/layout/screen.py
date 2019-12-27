from fluent.widget.layout import Spacer
from fluent.render import window


class Screen(Spacer):
    """A class used to represent an screen

    Parameters
    ----------
    child : Widget
        a root widget of the application
    """
    def __init__(self, child):
        self.child = child

        super(Screen, self).__init__(size=window.size)

    def build(self):
        return self.child
