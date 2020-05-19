import pygame,sys

class Ui:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 32)
        self.score = 0
        self.hiscore = 0
        
    def render(self, score, hiscore):
        self.scoretxt = self.font.render(f"Score: {score}",True,(0,128,0))
        self.hiscoretxt = self.font.render(f"HighScore: {hiscore}",True,(0,128,0))
        self.screen.blit(self.screen,(0,0))
        self.screen.blit(self.scoretxt,(0,0))
        self.screen.blit(self.hiscoretxt,(1000,0))
        print(f"hi {hiscore} ; score {score} - UI")