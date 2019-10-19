from os import environ
import pygame

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
pygame.init()

pygame.display.set_caption('Rocket')
surface = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('product_sans', 28)
clock = pygame.time.Clock()
touches = []


def update_touches():
    touches.clear()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            touches.append(event.pos)
