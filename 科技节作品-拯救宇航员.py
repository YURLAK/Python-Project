#导入模块
import pygame
import sys,time,random
from colorama import Fore
#初始化
pygame.init()#pygame初始化
pygame.display.init()#屏幕初始化
pygame.font.init()#字体初始化
#设置游戏窗口
screen = pygame.display.set_mode((450,450))#设置窗口对象screen，边长450
start_image = pygame.image.load('太空背景.png')#设置背景
screen.blit(start_image,(-100,3))#调整背景
pygame.display.set_caption('拯救宇航员')#设置窗口标题
#开始界面设置
font = pygame.font.Font(".ttf/字体.ttf",60)#设置‘拯救宇航员’的字体
font2 = pygame.font.Font(".ttf/字体.ttf",40)#设置‘空格开始’的字体
text = font.render("拯救宇航员",True,(20,0,255))#设置字体内容，颜色
text2 = font2.render("空格开始",True,(255,20,5))#设置字体内容，颜色
screen.blit(text, (100,80))#把两个文本推送到屏幕上
screen.blit(text2,(150,250))
pygame.display.flip()#更新窗口
while True:#进入游戏主循环
    for event in pygame.event.get():
        #检测是否按下‘X’键
        if event.type == pygame.QUIT:
            exit(0)#如果按下就退出
        elif event.type == pygame.KEYDOWN:#检测键盘是否被按下
            key_list = pygame.key.get_pressed()#获取键盘检测列表
            if key_list[pygame.K_SPACE]:#如果空格被按下就进入游戏
                pygame.display.init()
                screen.fill('black')
                #进入游戏
                #设置字体文件
                font_spaceman1 = pygame.font.Font('.ttf/字体.ttf',32)
                font_spaceman2 = pygame.font.Font('.ttf/字体.ttf',32)
                font_spaceman3 = pygame.font.Font('.ttf/字体.ttf',32)
                font_spaceman4 = pygame.font.Font('.ttf/字体.ttf',32)
                #设置字体内容
                text_spaceman1 = font_spaceman1.render("宇航员正要返回地球",True,(250,0,0))
                text_spaceman2 = font_spaceman2.render("可却发现返回舱内缺失了1个零件",True,(250,0,0))
                text_spaceman3 = font_spaceman3.render("帮助宇航员找回丢失的零件",True,(250,0,0))
                text_spaceman4 = font_spaceman4.render("WASD控制",True,(250,0,0))
                #推送文本到主屏幕
                screen.blit(text_spaceman1,(120,180))
                pygame.display.flip()
                time.sleep(2)
                screen.fill('black')

                screen.blit(text_spaceman2,(35,180))
                pygame.display.flip()
                time.sleep(2)
                pygame.display.init()
                screen.fill('black')

                screen.blit(text_spaceman3,(45,180))
                pygame.display.flip()
                time.sleep(3)
                screen.fill('black')

                screen.blit(text_spaceman4,(160,180))
                pygame.display.flip()
                time.sleep(2)
                screen.fill('black')

                pygame.display.flip()

                #导入宇航员图片
                spaceman1 = pygame.image.load('宇航员2.png')
                spaceman2 = pygame.image.load('宇航员.png')

                #导入零件图片
                l1 = pygame.image.load('零件1.png')

                #设置零件初始坐标
                l1x = random.randint(2,400)
                l1y = random.randint(2,400)

                #宇航员坐标初始化
                x = 194
                y = 186

                #推送宇航员到主屏幕
                screen.blit(spaceman1,(x,y))
                pygame.display.flip()

                print(Fore.RED+"检测雷达已开启...")
                time.sleep(1)

                starttime = time.time()
                #游戏主循环
                while True:
                    #设置零件与宇航员的坐标之差，用于比较距离
                    Y = l1y - y
                    X = l1x - x
                    print_xy = False
                    if X <= 5 and X >= -5 and Y <= 5 and Y >= -5:
                        endtime = round(time.time() - starttime)
                        print_xy = True
                        screen.blit(l1,(l1x+5,l1y+5))
                        screen.blit(spaceman1,(x-5,y-5))
                        time.sleep(3)
                        pygame.display.flip()
                        font_found = pygame.font.Font('.ttf/字体.ttf',30)
                        font_time = pygame.font.Font('.ttf/字体.ttf', 35)
                        text_found = font_found.render("恭喜你，找到了丢失零件！",True,(30,140,250))
                        text_time = font_time.render(f"耗时{endtime}秒",True,(0,10,250))

                        time.sleep(2)
                        pygame.display.init()
                        screen.fill('black')
                        screen.blit(text_found,(110,170))
                        pygame.display.flip()
                        time.sleep(2)

                        screen.fill('black')
                        screen.blit(text_time,(120,170))
                        pygame.display.flip()
                        time.sleep(2)
                        exit(0)

                    elif X <= 10 and X >= -10 and Y <= 10 and Y >= -10:
                        print(Fore.BLUE+"你快找到零件了！")

                    elif X <= 20 and X >= -20 and Y <= 10 and Y >= -20:
                        print(Fore.BLUE + "你离零件很近了！")

                    elif X <= 40 and X >= -40 and Y <= 40 and Y >= -40:
                        print(Fore.BLUE + "你和零件有一段距离了！")

                    else:
                        print(Fore.BLUE+"零件离你还很远！")

                    if print_xy == True:
                        print(Fore.RED+"检测雷达已关闭...")
                        break
                    #WASD控制宇航员
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit(0)
                        else:
                            key_list = pygame.key.get_pressed()
                            #W键
                            if key_list[pygame.K_w]:
                                y -= 1.5
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            #S键
                            elif key_list[pygame.K_s]:
                                y += 1.5
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            #A键
                            elif key_list[pygame.K_a]:
                                x -= 1.5
                                screen.blit(spaceman1,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
                            #D键
                            elif key_list[pygame.K_d]:
                                x += 1.5
                                screen.blit(spaceman2,(x,y))
                                pygame.display.flip()
                                screen.fill('black')
