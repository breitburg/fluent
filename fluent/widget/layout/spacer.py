from fluent.core.widget import RenderWidget


class Spacer(RenderWidget):
    """A class used to represent an spacer

    Parameters
    ----------
    size : tuple
        size of the spacer
    """

    def __init__(self, size):
        super(Spacer, self).__init__(size=size)
