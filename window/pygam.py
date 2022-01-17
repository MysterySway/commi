import pygame
import sys



#初始化pygame
pygame.init()

#背景面板
deep_screen = pygame.display.set_mode((500,500))

#标题
pygame.display.set_caption('hello world')


#颜色变量
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)

#使用颜色填充背景
deep_screen.fill(WHITE)

#加载资源
#图片
#player = pygame.image.load(namehint="player.png")
x,y = (178,504)
#背景
#background = pygame.image.load(namehint="background.png")


#定义FPS
FPS = 30
clock = pygame.time.Clock()

#主循环函数
while True:
    

    #对屏幕特定区域进行绘制
    #deep_screen.blit(background,(0,0))
    #deep_screen.blit(player,(0,0))
    #y -= 1

    #pygame.draw.circle(deep_screen,BLACK, (100,50), 30, width=0)
    #pygame.draw.line(deep_screen, BLACK, (150,130),(130,170), width=1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #循环进行刷新
    pygame.display.update()
    #设置FPS
    clock.tick(FPS)