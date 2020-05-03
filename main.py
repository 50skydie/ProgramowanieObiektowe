import pygame
import sys
from pygame.locals import *

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720
 
    def on_init(self): #init things, works only once at start
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size) 
        self._running = True
 
    def on_event(self, event): #events here
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self): #loop things here
        pass
    def on_render(self): #render thigns here
        pass
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