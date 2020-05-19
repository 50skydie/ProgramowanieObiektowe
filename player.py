import pygame,sys
from pygame.math import Vector2
from enemy import Enemy
class Player:

    def __init__(self):
        self.pos = Vector2(50,50)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.isdead = False
        
    def force(self,Force):
        self.acc += Force

    def addforce(self):
        self.force(Vector2(0,-10))

    def tick(self):
        self.vel += Vector2(0,0.1)
        #skok
        self.vel *= 0.8
        self.vel += self.acc
        self.pos += self.vel
        self.acc *=0
        if self.pos.y<0 :
            self.pos.y = 0
        if self.pos.y>=620:
            self.pos.y = 620    
        
    def draw(self,screen):
        if(self.isdead):
            screen.blit(pygame.transform.scale(pygame.image.load("spritesheets/BLANK.png"), (0, 0)), self.pos)
        else:
            screen.blit(pygame.transform.scale(pygame.image.load("spritesheets/Player.png"), (200, 100)), self.pos) 

    def collision(self,enemy):
        if (enemy._y_pos-100)<self.pos.y<(enemy._y_pos+100):
            if (enemy._x_pos-100)<self.pos.x<(enemy._x_pos+100):
                self.isdead = True

    def isDead(self):
        return self.isdead

    def click(self):
        self.isdead = False