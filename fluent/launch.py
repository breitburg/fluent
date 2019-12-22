from fluent.render import window
from fluent.widget.layout import Screen


def launch(target):  # App launching function
    target = Screen(child=target)  # Adding parent widget
    window.show()  # Showing window

    while True:
        target.render(xy=(0, 0))  # Rendering generic widget
        window.update()  # Updating window events, renderer and clearing
