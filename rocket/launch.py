from rocket.render import window
from rocket.widget.shapes import Spacer


def launch(target):  # App launching function
    window.show()  # Showing window
    target = target(Spacer(size=window.size))  # Initializing target object

    while True:
        target.render(xy=(0, 0))  # Rendering generic widget
        window.update()  # Updating window events, renderer and clearing
