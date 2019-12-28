from sdl2.ext import Renderer as SDL_Renderer, Window as SDL_Window, get_events
from sdl2.events import SDL_MOUSEBUTTONDOWN, SDL_QUIT
from sdl2.ext import SpriteFactory


class Window(SDL_Window):
    def __init__(self, title='Fluent Window', size=(640, 480), scale=1):
        super(Window, self).__init__(title=title, size=size)
        self.renderer = SDL_Renderer(target=self)  # Initializing renderer instance
        self.factory = SpriteFactory(renderer=self.renderer)  # Initializing sprite factory instance
        self.events = list()  # Events list
        self.scale = scale  # Setting scaling

    def update(self):
        self.events.clear()
        for event in get_events():
            if event.type == SDL_MOUSEBUTTONDOWN:
                self.events.append((event.button.x, event.button.y))
            elif event.type == SDL_QUIT:
                quit()

        self.renderer.present()  # Presenting renderer
        self.renderer.clear(color=(0, 0, 0, 255))  # Clearing renderer

        self.refresh()  # Refreshing window
