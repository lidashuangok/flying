# !usr/bin/python
# Author:das
# -*-coding: utf-8 -*-
import pygame,sys
class OurPlane(pygame.sprite.Sprite):
    energy = 50
    def __init__(self,bg_size):
        super(OurPlane,self).__init__()
        self.image_one = pygame.image.load("../material/image/hero1.png")
        #self.image_one = pygame.image.load("../material/image/hero1.png")
        self.image_two = pygame.image.load("../material/image/hero2.png")
        #self.image_two = pygame.image.load("../material/image/hero2.png")
        self.energy = OurPlane.energy
        #飞机位置
        self.rect = self.image_one.get_rect()
        #背景大小
        self.width,self.height = bg_size[0],bg_size[1]
        #飞机位置
        self.rect.left,self.rect.top= (self.width - self.rect.width)//2,self.height-self.rect.height-30
        #self.rect.left, self.rect.top = \
            #(self.width - self.rect.width) // 2, (self.height - self.rect.height) - 40
        # 获取飞机图片的掩膜，用来精准碰撞检测

        self.mask = pygame.mask.from_surface(self.image_one)
        # 设置飞机的移动速度单位
        self.speed = 10
        # 设置飞机的生命状态， True 活的，False  死的
        self.active = True
         # 加载飞机损毁状态
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("../material/image/hero_blowup_n4.png"),
            pygame.image.load("../material/image/hero_blowup_n3.png"),
            pygame.image.load("../material/image/hero_blowup_n2.png"),
            pygame.image.load("../material/image/hero_blowup_n1.png")
            ]
        )


    #飞机向下移动
    def move_down(self):
        if self.rect.bottom < self.height:
            self.rect.bottom +=self.speed
        else:
            self.rect.bottom = self.height


    def move_UP(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    # 飞机向下移动
    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right== self.width

    def reset(self):
        self.rect.left,self.rect.top= (self.width - self.rect.width)//2,self.height-self.rect.height-30
        self.active = True