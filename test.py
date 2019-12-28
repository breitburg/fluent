from fluent.essential import *  # Importing library


class MyOwnWidget(Widget):
    def build(self):
        print(self.parent)
        return Align(Text('Hello', color=ColorProperty.white), align=(AlignProperty.center, AlignProperty.center))


launch(target=MyOwnWidget())
