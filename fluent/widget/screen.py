from fluent.core.widget import GenericWidget


class Screen(GenericWidget):
    def __init__(self, size: tuple):
        super(Screen, self).__init__(size=size)
