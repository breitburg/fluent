from fluent.core.launch import launch
from fluent.core.property import Color
from fluent.widget.shape import Text
from fluent.core.widget import Widget
from fluent.core.debug import auto_reload


@auto_reload
class TestWidget(Widget):
    def build(self) -> object:
        return Text(text='Hello, world', color=Color(255, 255, 255))


launch(
    target=TestWidget()
)