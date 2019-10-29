class Widget:
    size: tuple = None

    def __init__(self, context):
        self.context = context
        self._update_instance()

    def build(self, context):
        return NotImplemented

    def render(self, xy):
        self._update_instance()
        self._instance.render(xy=xy)

    def _update_instance(self):
        self._instance = self.build(context=self.context)
        self.size = self._instance.size


class GenericWidget(Widget):
    def __init__(self, size):
        self.size = size
        super(GenericWidget, self).__init__(self)

    def build(self, context):
        return self
