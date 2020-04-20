import pygame
import sys
pygame.init()

size = width, height = 600, 800
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#Game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    pygame.display.flip()
