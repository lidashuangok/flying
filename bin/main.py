# !usr/bin/python
# Author:das
# -*-coding: utf-8 -*-
""""程序入口，主程序"""
import pygame
from pygame.locals import *
import sys
from src.plane import OurPlane
from src.enemy import SmallEnemy
from src.bullet import Bullet
from src.midenemy import MidEnemy
from src.bossenemy import Boss
from src.enemybull import BossBullet



bg_size = (480,700)
pygame.init()
screen = pygame.display.set_mode((480,700))
pygame.display.set_caption("airplane war")
bgp = pygame.image.load("../material/image/background.png").convert()
pause = pygame.image.load("../material/image/game_pause_pressed.png")
start = pygame.image.load("../material/image/startpic.png")
end = pygame.image.load("../material/image/game_over.png")

color_black = (0,0,0)
color_green = (7,220,0)
color_red = (232,16,16)
color_white = (255,255,255)

ourplane = OurPlane(bg_size)
smallenemy = SmallEnemy(bg_size)
boss = Boss(bg_size)
#bul = Bullet(ourplane.rect)

score = 0

def add_shot(group1,num):
    for i in range(num):
        bul = Bullet(ourplane.rect)
        group1.add(bul)

def add_SmallEnemy(group1,group2,num):
    for i in range(num):
        smallenemy = SmallEnemy(bg_size)
        group1.add(smallenemy)
        group2.add(smallenemy)
def endgame(score):
    print(score)
    font = pygame.font.SysFont("", 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(end, (0, 0))
        text_surface = font.render(str(score), True, (0, 0, 0))
        screen.blit(text_surface, (200, 380))
        pygame.display.update()



def startup():
    while True:
        screen.blit(start, (0,0))
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            #print(x,y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 330 and x>130 and y>484 and y<541:
                    main()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()



def main():
    y = 0
    running = True
    switch_image = False
    delay = 60
    font = pygame.font.SysFont("", 30)
    enemis = pygame.sprite.Group()
    smallenemies = pygame.sprite.Group()
    add_SmallEnemy(enemis, smallenemies,6)

    bulls = pygame.sprite.Group()
    bossbulls = pygame.sprite.Group()


    while running:
        screen.blit(bgp, (0, y - 700))
        screen.blit(bgp, (0, y))
        delay-= 1
        text_surface = font.render("score:"+str(score), True, (0, 0, 0))
        screen.blit(text_surface, (385, 5))
        if delay ==0:
            delay = 60
        if delay % 3:
            switch_image = not switch_image


        #我方
        if ourplane.active:
            if switch_image :
                screen.blit(ourplane.image_one,ourplane.rect)
            else:
                screen.blit(ourplane.image_two, ourplane.rect)
        else:
            screen.blit(ourplane.destroy_images[delay%4], ourplane.rect)
            ourplane.reset()

        clock = pygame.time.Clock()
        clock.tick(30)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            ourplane.move_UP()
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            ourplane.move_left()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            ourplane.move_right()
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            ourplane.move_down()

        y+= 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #global running
                    running = False
                    while True:
                        #screen.blit(pause,(100,100))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    running = True
                                    break
                                    #print(running)
                        if running:
                            break
                        screen.blit(pause, (240, 420))
                        pygame.display.update()
                        #print(running)
                        #break
                    # pygame.display.update()

        if y == 700:
            y=0

        #子弹
        if delay % 5==0:
            # bul = Bullet(ourplane.rect)
            # bul.update()
            # screen.blit(bul.image,bul.rect)
            bul = Bullet(ourplane.rect)
            bulls.add(bul)
        bulls.update()
        bulls.draw(screen)

        #敌机
        if score<100:
            if delay % 30==0:
                enemy = SmallEnemy(bg_size)
                enemis.add(enemy)
            if delay % 60==0:
                enemy = MidEnemy(bg_size)
                enemis.add(enemy)
        enemis.update()
        enemis.draw(screen)

        if score >= 100:
            if delay % 10 == 0:
                bul = BossBullet(boss.rect)
                bossbulls.add(bul)
            bossbulls.update()
            bossbulls.draw(screen)

            energy_remain = boss.energy / Boss.energy
            if energy_remain > 0.2 :
                energy_color = color_green
            else:
                energy_color = color_red
            pygame.draw.line(screen,color_black,(boss.rect.left, boss.rect.bottom + 5),
                                 (boss.rect.right, boss.rect.bottom +5), 5)
            pygame.draw.line(screen, energy_color, (boss.rect.left, boss.rect.bottom + 5),
                             (boss.rect.left+(boss.rect.right-boss.rect.left)*energy_remain, boss.rect.bottom+ 5), 5)
            boss.update()
            screen.blit(boss.image,boss.rect)
        #画血条
        for each in enemis:
            energy_remain = each.energy / each.energy_in
            if energy_remain > 0.2:
                energy_color = color_green
            else:
                energy_color = color_red
            pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top- 5),
                             (each.rect.right, each.rect.top - 5), 5)
            pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                             (
                                 each.rect.left + (each.rect.right - each.rect.left) * energy_remain, each.rect.top - 5),
                             5)

        collide_list = pygame.sprite.groupcollide(enemis,bulls , False, True,pygame.sprite.collide_mask)
        for enemy in collide_list:
            enemy.energy -=1
            global score
            score += 1
            if enemy.energy <= 0:
                for i in range(4):
                    screen.blit(enemy.destroy_images[i],enemy.rect)
                enemis.remove(enemy)
        if pygame.sprite.spritecollide(ourplane, enemis, True,pygame.sprite.collide_mask):
            ourplane.energy -= 1
        if pygame.sprite.spritecollide(ourplane, bossbulls, True,pygame.sprite.collide_mask):
            ourplane.energy -= 1
        if pygame.sprite.spritecollide(boss, bulls, True,pygame.sprite.collide_mask):
            boss.energy -= 1
            if boss.energy <=0:
                running = False
                endgame(score)
        energy_remain = ourplane.energy / OurPlane.energy
        if energy_remain > 0.2:
            energy_color = color_green
        else:
            energy_color = color_red
        pygame.draw.line(screen, color_black, (ourplane.rect.left, ourplane.rect.top - 5),
                         (ourplane.rect.right, ourplane.rect.top - 5), 5)
        pygame.draw.line(screen, energy_color, (ourplane.rect.left, ourplane.rect.top - 5),
                         (ourplane.rect.left+(ourplane.rect.right-ourplane.rect.left)*energy_remain, ourplane.rect.top - 5), 5)

        pygame.display.update()
        #print(score)
if __name__ == '__main__':
    startup()
    #main()


