from rocket import widget, render, layout

from pygame import event, QUIT, display


def run_app(widget):
    while True:
        widget.build().render(xy=(0, 0))
        for i in event.get():
            if i.type == QUIT: exit()
        display.update()
        render.surface.fill(color=(0, 0, 0))
        render.clock.tick(60)
