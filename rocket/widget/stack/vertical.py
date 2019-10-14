from rocket.widget.stack import Stack


class VerticalStack (Stack):
    def __init__(self, widgets, spacing=0):
        super(VerticalStack, self).__init__(
            widgets=widgets, spacing=spacing, coordinate=1
        )
