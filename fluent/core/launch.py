from fluent.core.window import window
from fluent.widget.screen import Screen


def launch(target: object):  # App launching function
    target.parent = Screen(size=window.size)  # Widget
    window.show()  # Showing window

    while True:
        target.render(xy=(0, 0))  # Rendering generic widget
        window.update()
