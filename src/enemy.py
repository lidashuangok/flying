# !usr/bin/python
# Author:das
# -*-coding: utf-8 -*-
import pygame,sys
from random import randint
class SmallEnemy(pygame.sprite.Sprite):
    energy = 1
    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load("../material/image/enemy1.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left,self.rect.top= randint(0,int(bg_size[0]-self.rect.width)),-self.rect.height
        #self.rect.left,self.rect.top= bg_size[0]-self.rect.width,0

        self.mask = pygame.mask.from_surface(self.image)
        # 设置飞机的移动速度单位
        self.speed = 2
        # 设置飞机的生命状态， True 活的，False  死的
        self.active = True
        self.energy = SmallEnemy.energy
        self.energy_in = SmallEnemy.energy
        #self.energy =0.1
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("../material/image/enemy1_down1.png"),
            pygame.image.load("../material/image/enemy1_down2.png"),
            pygame.image.load("../material/image/enemy1_down3.png"),
            pygame.image.load("../material/image/enemy1_down4.png")
        ]
        )
    def reset(self):
        #self.rect.left,self.rect.top= (self.width - self.rect.width)//2,self.height-self.rect.height-30
        self.rect.left,self.rect.top= randint(0,self.width-self.rect.width),-self.rect.height

        self.active = True
    def update(self):
        if self.rect.top < self.height:
            self.rect.top+=self.speed
        else:
            #self.rect.bottom = self.height
            self.reset()