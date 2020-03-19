from fluent.core.window import window


def launch(target: object):  # App launching function
    window.show()  # Showing window

    while True:
        target.render(xy=(0, 0))  # Rendering generic widget
        window.update()
