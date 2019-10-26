from os import environ, path
import pygame

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
pygame.init()

pygame.display.set_caption('Rocket')
surface = pygame.display.set_mode((400, 650))

font_regular = pygame.font.Font(path.join(
    __file__.replace(path.join('render', '__init__.py'), ''),
    'font', 'product_sans_regular.ttf'), 26)
font_bold = pygame.font.Font(path.join(
    __file__.replace(path.join('render', '__init__.py'), ''),
    'font', 'product_sans_bold.ttf'), 26)

clock = pygame.time.Clock()
touches = []


def update_touches():
    touches.clear()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            touches.append(event.pos)
        elif event.type == pygame.QUIT:
            quit()
