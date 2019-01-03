# !usr/bin/python
# Author:das
# -*-coding: utf-8 -*-
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Bullet, self).__init__()
        self.image = pygame.image.load("../material/image/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos[0]+45,pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        # 设置飞机的移动速度单位
        self.speed = 50
        # 设置飞机的生命状态， True 活的，False  死的
        self.active = True

    def reset(self):
        # self.rect.left,self.rect.top= (self.width - self.rect.width)//2,self.height-self.rect.height-30
        #self.rect.left, self.rect.top = randint(0, int(self.width - self.rect.width)), -self.rect.height
        self.active = True
    def update(self):
        if self.rect.top > 0:
            self.rect.top-=self.speed
            #print(self.rect.top,self.speed)
        else:
            self.kill()
            #self.rect.bottom = self.height
            #self.active = False