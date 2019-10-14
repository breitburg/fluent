from rocket import widget, render
from pygame import event, QUIT, display


def run_app(widget):
    while True:
        widget.build().render(xy=(0, 0))
        for i in event.get():
            if i.type == QUIT: exit()
        display.update()
