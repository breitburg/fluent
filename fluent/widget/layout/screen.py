from fluent.widget.layout import Spacer
from fluent.render import window


class Screen(Spacer):
    def __init__(self, child):
        self.child = child

        super(Screen, self).__init__(size=window.size)

    def build(self):
        return self.child
