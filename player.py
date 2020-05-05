import pygame,sys
from pygame.math import Vector2
from enemy import Enemy
class Player(object):

    def __init__(self, Game):
        self.Game=Game
        size = self.Game.screen.get_size()
        self.pos = Vector2(size[0]/3,size[1]/3)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.screen = self.Game.screen
        
   
    def force(self,Force):
        self.acc += Force

    def tick(self):
        #input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.force(Vector2(0,-1))
        #opor
        self.vel *= 0.9
        #grawitacja
        self.vel += Vector2(0,0.5)
        #skok
        self.vel += self.acc
        self.pos += self.vel
        self.acc *=0
        

    def draw(self):
        rect = pygame.Rect(self.pos.x,self.pos.y,50,50)
        pygame.draw.rect(self.Game.screen,(0,150,255),rect)


    def collision(self):
        self.enemy = Enemy(self)
        if (self.enemy.pos.y-40)<self.pos.y<(self.enemy.pos.y+40):
            if (self.enemy.pos.x-40)<self.pos.x<(self.enemy.pos.x+40):
                exit(0)
            
        
        
