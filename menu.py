#!/usr/bin/env python

import sys
if sys.version_info < (3, 8):
    sys.exit("Need to run in python 3.8!")

import pygame
if not pygame.init():
    sys.exit("pygame can not be initialized!")

from enemy import *
from random import *
from player import *
from score_system import *
from menu import *

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.text = self.font.render("Start",True,(0,128,0))
        self.ismenuon = True
        self.ellipse = pygame.draw.ellipse(self.screen,22,(500,300,300,150))

    def render(self):
        surface2 = pygame.transform.rotate(self.screen, 360)
        self.screen.blit(self.screen,(0,0))
        self.screen.blit(self.text,(550,320))

    def onloop(self, isgameon):
        x,y = pygame.mouse.get_pos()
        if self.ellipse.collidepoint((x,y)):
            self.ismenuon = True 
   
    def click(self):
        self.ismenuon = False

    def ismenuon(self):
        return self.ismenuon