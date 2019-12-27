from fluent.widget import GenericWidget


class Stack(GenericWidget):
    def __init__(self, children, coordinate, spacing=10):
        self.children = children
        self.spacing = spacing
        self.__coordinate__ = coordinate

        super(Stack, self).__init__(size=self.calculate_size())

    def calculate_size(self):
        size = [0, 0]
        for widget in self.children:
            size[1] += widget.size[1] + self.spacing
            size[0] = max(size[0], widget.size[0])
        return size

    def render(self, xy):
        offset = [0, 0]

        for widget in self.children:
            widget.render(
                xy=(
                    offset[0] + xy[0],
                    offset[1] + xy[1]
                )
            )
            offset[self.__coordinate__] += widget.size[self.__coordinate__] + self.spacing


class Row(Stack):
    """A class used to represent an row

    Parameters
    ----------
    children : list<Widget>
        widgets that will be displayed in a row

    spacing : int
        amount of spacing we apply to children
    """

    def __init__(self, children, spacing=10):
        super(Row, self).__init__(children=children, spacing=spacing, coordinate=0)


class Column(Stack):
    """A class used to represent an column

    Parameters
    ----------
    children : list<Widget>
        widgets that will be displayed in a column

    spacing : int
        amount of spacing we apply to children
    """

    def __init__(self, children, spacing=10):
        super(Column, self).__init__(children=children, spacing=spacing, coordinate=1)
