import pygame
import sys
from pygame.locals import *
from random import *

class Enemy:
    def __init__(self):
        self._enemy_image = pygame.image.load("spritesheets/enemy1.png")
        self._speed = 1
        self._points = 25
        self._x_pos = 1280
        self._y_pos = randrange(0, 620)
        self._starting_pos = (self._x_pos, self._y_pos) # generating enemy at max right and random height
    
    def renderEnemy(self, display_surf):
        display_surf.blit(pygame.transform.scale(self._enemy_image, (200, 100)), self._starting_pos)

    def enemyMovment(self):
        self._x_pos -= self._speed
        self._starting_pos = (self._x_pos, self._y_pos) # can this be more optimal?

    def outOfBoundry(self):
        #pseudo auto generating objects XDDD
        if(self._x_pos < -500):
            self._x_pos = 1280
            self._y_pos = randrange(0, 620)