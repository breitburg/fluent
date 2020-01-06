class Color:
    def __init__(self, red, green, blue, alpha=255):
        self.rgba = red, green, blue, alpha

    def __add__(self, other) -> object:
        return Color(red=self.rgba[0] + other.rgba[0], green=self.rgba[1] + other.rgba[1],
                     blue=self.rgba[2] + other.rgba[2], alpha=self.rgba[3] + other.rgba[3])


class Weight:
    def __init__(self, string: str):
        self.string = string

    def __add__(self, other) -> object:
        return Weight(string=' '.join((self.string, other.string)))
