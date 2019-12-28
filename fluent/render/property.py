class Color:
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    white = (255, 255, 255, 255)
    black = (0, 0, 0, 255)
    transparent = (0, 0, 0, 0)

    def rgb(red, green, blue, alpha=255):
        return red, green, blue, alpha


class Aligner:
    top = 'top'
    bottom = 'bottom'
    left = 'left'
    right = 'right'
    center = 'center'


class Weight:
    regular = 'regular'
    bold = 'bold'
    italic = 'italic'
