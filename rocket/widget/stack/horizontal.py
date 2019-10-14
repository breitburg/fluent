from rocket.widget.stack import Stack


class HorizontalStack (Stack):
    def __init__(self, widgets, spacing=0):
        super(HorizontalStack, self).__init__(
            widgets=widgets, spacing=spacing, coordinate=0
        )
