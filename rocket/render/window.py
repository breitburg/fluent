from sdl2.ext import Renderer as SDL_Renderer, Window as SDL_Window, get_events


class Window(SDL_Window):
    def __init__(self, title='Rocket Window', size=(640, 480)):
        super(Window, self).__init__(title=title, size=size)
        self.renderer = SDL_Renderer(target=self)   # Initializing renderer instance
        self.events = list()  # Events list

    def update(self):
        self.events = get_events()  # Updating events

        self.renderer.present()  # Presenting renderer
        self.renderer.clear((0, 0, 0, 255))  # Clearing renderer

        self.refresh()  # Refreshing window
