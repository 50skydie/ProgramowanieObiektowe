import pygame
import sys
from pygame.locals import *
from enemy import *
from random import *

#there are too much comments, but they can be helpful
class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self.weight, self.height = 1280, 720
        self._background_image = None
        self._enemies = [Bird(), Crow()]
        self._enemy_id = (randrange(0,100) % 2)
 
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
        self._enemies[self._enemy_id].enemyMovment()
        if(self._enemies[self._enemy_id].isOutOfBoundry()): #reseting enemies with random class 0 = bird 1 = crow after crossing boundary,
            self._enemy_id = (randrange(0,100) % 2)
            self._enemies[self._enemy_id].resetPosition()

    def on_render(self): #render thigns here
        self._display_surf.blit(self._background_image, [0,0])
        self._enemies[self._enemy_id].renderEnemy(self._display_surf) 
        pygame.display.flip()

    def on_cleanup(self): #just cleaning modules
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
 
 #maybe some req here
if __name__ == "__main__" :
    theGame = Game()
    theGame.on_execute()
pygame.quit()