from fluent.essential import *  # Importing library


class MyOwnWidget(Widget):
    def build(self):
        # print(self.parent)
        return Align(Text('Hello', color=Color.white), align=(Aligner.center, Aligner.center))


launch(target=MyOwnWidget())
