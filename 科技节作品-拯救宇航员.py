#import blocks
import pygame
import sys,time,random
from colorama import Fore
#init
pygame.init()#init pygame
pygame.display.init()#init display
pygame.font.init()#init font
yes_or_no_start = False
yes_or_no_level_1 = False
x = 100
y = 100
#set window
screen = pygame.display.set_mode((450,450))#init window
start_image = pygame.image.load('太空背景.png')
screen.blit(start_image,(-100,3))
pygame.display.set_caption('拯救宇航员')#init title
#started codes!
font = pygame.font.SysFont("simHei",40)
text = font.render("拯救宇航员",True,(200,250,255))
font2 = pygame.font.SysFont("simHei",35)
text2 = font2.render("空格开始",True,(250,20,0),(0,0,0))
pygame.display.flip()#update window
screen.blit(text, (120,80))
screen.blit(text2,(150,250))
pygame.display.flip()
while yes_or_no_start == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_SPACE]:
                pygame.display.init()
                screen.fill('black')
                #two texts
                #set font3 and font 4
                number = 0
                font3 = pygame.font.SysFont("simHei", 20)
                font4 = pygame.font.SysFont('simHei', 20)
                font5 = pygame.font.SysFont('microsoft Yahei',50)
                font6 = pygame.font.SysFont('simHei', 20)
                font7 = pygame.font.SysFont("simHei",20)
                #plus the text
                text_spaceman_back_earth = font3.render("宇航员正要返回地球", True, (250, 0, 0))
                text_spaceman_back_earth2 = font4.render("可却发现自己遇到了重重困难...", True, (250, 0, 0))
                text_spaceman_back_earth3 = font5.render("Level1",True,(0,0,250))
                text_spaceman_back_earth4 = font6.render("帮助宇航员找回丢失的1个零件,WASD控制",True,(250,0,0))
                #blit it
                screen.blit(text_spaceman_back_earth,(130,180))
                pygame.display.flip()
                time.sleep(2)
                screen.fill('black')
                screen.blit(text_spaceman_back_earth2,(120,180))
                pygame.display.flip()
                time.sleep(2)
                pygame.display.init()
                screen.fill('black')
                screen.blit(text_spaceman_back_earth3,(185,185))
                pygame.display.flip()
                time.sleep(2)
                pygame.display.init()
                screen.fill('black')
                screen.blit(text_spaceman_back_earth4,(70,180))
                pygame.display.flip()
                time.sleep(3)
                pygame.display.init()
                screen.fill('black')
                pygame.display.flip()
                spaceman1 = pygame.image.load('宇航员2.png')
                spaceman2 = pygame.image.load('宇航员.png')
                l1 = pygame.image.load('零件1.png')
                #设置三个零件的坐标
                l1x = random.randint(2,400)
                l1y = random.randint(2,400)
                x = 194
                y = 186
                screen.blit(spaceman1,(x,y))
                pygame.display.flip()
                print(Fore.RED+"检测雷达已开启...")
                time.sleep(1)
                while True:
                    Y = l1y - y
                    X = l1x - x
                    if X <= 2 and X >= -2 and Y <= 2 and Y >= -2:
                        exit(0)
                    print(Fore.BLUE+f"x坐标差{X}"," ",f"y坐标差{Y}")
                    #screen.blit(l1,(l1x,l1y))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit(0)
                        else:
                            key_list = pygame.key.get_pressed()
                            if key_list[pygame.K_w]:
                                y -= 1
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            elif key_list[pygame.K_s]:
                                y += 1
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            elif key_list[pygame.K_a]:
                                x -= 1
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            elif key_list[pygame.K_d]:
                                x += 1
                                screen.blit(spaceman2,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
