from rocket.widget.core import CoreWidget


class Stack (CoreWidget):
    def __init__(self, widgets, spacing=0, coordinate=0):
        super(Stack, self).__init__()

        self.widgets = widgets
        self.spacing = spacing
        self.__coordinate__ = coordinate

    def render(self, xy):
        offset = [0, 0]
        rectangle = [0, 0]

        for widget in self.widgets:
            size = widget.build().render(xy=(xy[0] + offset[0], xy[1] + offset[1]))
            offset[self.__coordinate__] += size[self.__coordinate__] + self.spacing

            rectangle[0], rectangle[1] = rectangle[0] + size[0], rectangle[1] + size[1]
            rectangle[self.__coordinate__] += self.spacing

        return rectangle[0], rectangle[1]
