import pygame
import sys
from pygame.locals import *
from enemy import *
from random import *
from player import Player

#there are too much comments, but they can be helpful
class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self.weight, self.height = 1280, 720
        self._background_image = None
        self._enemies = [Bird(), Crow()]
        self._enemy_id = (randrange(0,100) % 2)
        self._player = Player()
 
    def on_init(self): #init things, works only once at start
        pygame.init()
        pygame.display.set_caption("ProgramowanieObiektowe")
        self._display_surf = pygame.display.set_mode(self._size) 
        self._running = True
        self._background_image = pygame.transform.scale(pygame.image.load("spritesheets/background.png").convert(), (1280, 720))
 
    def on_event(self, event): #events here
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self): #loop things here
        self._enemies[self._enemy_id].enemyMovment()
        if(self._enemies[self._enemy_id].isOutOfBoundry()): #reseting enemies with random class 0 = bird 1 = crow after crossing boundary,
            self._enemy_id = (randrange(0,100) % 2)
            self._enemies[self._enemy_id].resetPosition()
        self._player.collision(self._enemies[self._enemy_id])
        self._player.tick()

    def on_render(self): #render thigns here
        self._display_surf.blit(self._background_image, [0,0])
        self._player.draw(self._display_surf)
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
if __name__ == "__main__":
    while True: 
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Programowanie Objektowe")
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Start",True,(0,128,0))
        tapeta = pygame.transform.scale(pygame.image.load("spritesheets/background.png").convert(), (1280, 720))
        screen.blit(tapeta,(0,0))
        x,y = pygame.mouse.get_pos()
        ellipse = pygame.draw.ellipse(screen,22,(500,300,300,150))
        surface2 = pygame.transform.rotate(screen, 360)
        screen.blit(screen,(0,0))
        screen.blit(text,(550,320))
        pygame.display.flip()
        if ellipse.collidepoint((x,y)):
            if click:
                theGame = Game()
                theGame.on_execute()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True