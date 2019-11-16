from fluent.render import window


def launch(target):  # App launching function
    window.show()  # Showing window

    while True:
        target.render(xy=(0, 0))  # Rendering generic widget
        window.update()  # Updating window events, renderer and clearing
