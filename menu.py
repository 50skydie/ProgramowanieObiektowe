import sys
import pygame

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

    def onloop(self, isplayerdead):
        if(isplayerdead):
            self.ismenuon = True

    def click(self):
        self.ismenuon = False
        #reset

    def ismenuon(self):
        return self.ismenuon