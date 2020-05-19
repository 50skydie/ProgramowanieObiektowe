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

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self.weight, self.height = 1280, 720
        self._background_image = None
        self._enemies = [Bird(), Crow()]
        self._enemy_id = (randrange(0,100) % 2)
        self._player = Player()
        self._laderboard = Score_system()
 
    def on_init(self):
        pygame.display.set_caption("ProgramowanieObiektowe")
        self._display_surf = pygame.display.set_mode(self._size) 
        self._menu = Menu(self._display_surf)
        self._running = True
        self._background_image = pygame.transform.scale(pygame.image.load("spritesheets/background.png").convert(), (1280, 720))
        self._laderboard.load_hiscore()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_reset()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self._player.addforce()

    def on_loop(self):
        if(self._menu.ismenuon):
            pass
        else:
            self._enemies[self._enemy_id].enemyMovment()
            if(self._enemies[self._enemy_id].isOutOfBoundry()):
                self._enemy_id = (randrange(0,100) % 2)
                self._enemies[self._enemy_id].resetPosition()
                self._laderboard.score_update(self._enemies[self._enemy_id].returnPoints())
            self._player.collision(self._enemies[self._enemy_id])
            self._player.tick()
            self._menu.onloop(self._player.isdead)

    def on_render(self):
        self._display_surf.blit(self._background_image, [0,0])
        if(self._menu.ismenuon):
            self._menu.render()
        else:
            self._player.draw(self._display_surf)
            self._enemies[self._enemy_id].renderEnemy(self._display_surf) 
        pygame.display.flip()

    def on_reset(self): #laderboard here
        self._menu.click()
        self._player.click()
        self._enemies[self._enemy_id].resetPosition()
        self._laderboard.set_hiscore()
        self._laderboard.save_hiscore()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self): 
        if self.on_init() == False:
            self._running = False
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute() 