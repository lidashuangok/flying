# !usr/bin/python
# Author:das
# -*-coding: utf-8 -*-
import pygame
bg_size = (480,700)
class BossBullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(BossBullet, self).__init__()
        self.image = pygame.image.load("../material/image/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos[0]+90,pos[1]+50
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 40
        # 设置飞机的生命状态， True 活的，False  死的
        self.active = True

    def reset(self):
        # self.rect.left,self.rect.top= (self.width - self.rect.width)//2,self.height-self.rect.height-30
        #self.rect.left, self.rect.top = randint(0, int(self.width - self.rect.width)), -self.rect.height
        self.active = True
    def update(self):
        if self.rect.top < bg_size[1]:
            self.rect.top+=self.speed
            #print(self.rect.top,self.speed)
        else:
            self.kill()
            #self.rect.bottom = self.height
            #self.active = False