from os import environ
import pygame

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
pygame.init()

pygame.display.set_caption('Rocket')
surface = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('arial', 36)
