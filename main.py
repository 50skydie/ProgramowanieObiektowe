import pygame
import sys
from pygame.locals import *
from enemy import Enemy
from random import *

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self.weight, self.height = 1280, 720
        self._background_image = None
        self._num_of_enemies = 1
        self._enemies = []
        for i in range(self._num_of_enemies): 
            self._enemies.append(Enemy())
 
    def on_init(self): #init things, works only once at start
        pygame.init()
        pygame.display.set_caption("ProgramowanieObiektowe")
        self._display_surf = pygame.display.set_mode(self._size) 
        self._running = True
        self._background_image = pygame.image.load("spritesheets/tmp_bg.jpg").convert()
 
    def on_event(self, event): #events here
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self): #loop things here
        for i in range(self._num_of_enemies): 
            self._enemies[i].enemyMovment()
            self._enemies[i].outOfBoundry()
    def on_render(self): #render thigns here
        self._display_surf.blit(self._background_image, [0,0])
        for i in range(self._num_of_enemies):
            self._enemies[i].renderEnemy(self._display_surf) 
        pygame.display.flip()
    def on_cleanup(self): #just cleaning modules
        pygame.quit()
 
    def on_execute(self): #starts final game
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
 #maybe some req here
if __name__ == "__main__" :
    theGame = Game()
    theGame.on_execute()
pygame.quit()