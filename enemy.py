import pygame
import sys
from pygame.locals import *
from random import *

#Parent class
class Enemy:
    def __init__(self):
        self._enemy_image = None
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

    def resetPosition(self):
        self._x_pos = 1280
        self._y_pos = randrange(0, 620)

    def isOutOfBoundry(self):
        if(self._x_pos < -500):
            return True

    def returnPoints(self):
        return self._points

#inheritance example
class Bird(Enemy):
    def __init__(self):
        super().__init__()
        #overdrive attributes
        self._speed = 0.5
        self._y_speed = 0.5
        self._points = 50
        self._enemy_image = pygame.image.load("spritesheets/enemy1.png")
    
    #overdrive method
    def enemyMovment(self):
        self._x_pos -= self._speed
        if(self._y_pos > 620):
            self._y_speed = -self._y_speed
        elif(self._y_pos < 0 ):
            self._y_speed = -self._y_speed
        self._y_pos += self._y_speed
        self._starting_pos = (self._x_pos, self._y_pos) # can this be more optimal tho?

#2nd class simple "copy paste" of parent class
class Crow(Enemy):
    def __init__(self):
        super().__init__()
        #need to change to other img
        self._enemy_image = pygame.image.load("spritesheets/enemy1.png")