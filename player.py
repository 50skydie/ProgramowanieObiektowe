import pygame,sys
from pygame.math import Vector2
from enemy import Enemy
class Player:

    def __init__(self):
        self.pos = Vector2(50,50)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        
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
        
    def draw(self,screen):
        screen.blit(pygame.transform.scale(pygame.image.load("spritesheets/enemy1.png"), (200, 100)), self.pos) 

    def collision(self):
        self.enemy = Enemy()
        if (self.enemy._y_pos-40)<self.pos.y<(self.enemy._y_pos+40):
            if (self.enemy._x_pos-40)<self.pos.x<(self.enemy._x_pos+40):
                print("wykryto kolizje")
            