class Widget:
    def __init__(self, context):
        self.__context__ = context
        self.__update_instance__()

    def build(self, context):
        return NotImplemented

    def render(self, xy):
        self.__update_instance__()
        self.__instance__.render(xy=xy)

    def __update_instance__(self):
        self.__instance__ = self.build(context=self.__context__)
        self.size = self.__instance__.size


class GenericWidget(Widget):
    def __init__(self, size):
        self.size = size
        super(GenericWidget, self).__init__(self)

    def build(self, context):
        return self
