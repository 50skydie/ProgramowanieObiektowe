import pygame
import sys
from random import *

class Enemy:
    def __init__(self):
        self._enemy_image = None
        self._speed = 1
        self._points = 25
        self._x_pos = 1280
        self._y_pos = randrange(0, 620)
        self._starting_pos = (self._x_pos, self._y_pos)
    
    def renderEnemy(self, display_surf):
        display_surf.blit(pygame.transform.scale(self._enemy_image, (200, 100)), self._starting_pos)

    def enemyMovment(self):
        self._x_pos -= self._speed
        self._starting_pos = (self._x_pos, self._y_pos)

    def resetPosition(self):
        self._x_pos = 1280
        self._y_pos = randrange(0, 620)

    def isOutOfBoundry(self):
        if(self._x_pos < -500):
            return True

    def returnPoints(self):
        return self._points

class Bird(Enemy):
    def __init__(self):
        super().__init__()
        self._speed = 0.5
        self._y_speed = 0.5
        self._points = 50
        self._enemy_image = pygame.image.load("spritesheets/Bird.png")
    
    def enemyMovment(self):
        self._x_pos -= self._speed
        if(self._y_pos > 620):
            self._y_speed = -self._y_speed
        elif(self._y_pos < 0 ):
            self._y_speed = -self._y_speed
        self._y_pos += self._y_speed
        self._starting_pos = (self._x_pos, self._y_pos)

class Crow(Enemy):
    def __init__(self):
        super().__init__()
        self._enemy_image = pygame.image.load("spritesheets/Crow.png")