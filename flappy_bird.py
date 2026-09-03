
import time
import pygame
from pygame.locals import *

pygame.init()

WIDTH = 864
HEIGTH =936

screen = pygame.display.set_mode((WIDTH,HEIGTH))

pygame.display.set_caption("Flappy bird :D")

city = pygame.image.load("city.png")
flying = False
ground = pygame.image.load("ground.png")
ground_scroll = 0
scroll_speed = 4
fps = 60
clock = pygame.time.Clock()
gameover = False

class Birb(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"birb{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False

    def update(self):


        # gravity
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            # print(f"bird vel = {self.vel}")
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

            

        #jump
        if gameover == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # handel animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #birb rotate
            self.image = pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)
        
birb_group = pygame.sprite.Group()

flappy = Birb(100,int(HEIGTH/2))
birb_group.add(flappy)

while True:
    clock.tick(fps)
    screen.blit(city,(0,0))

    birb_group.draw(screen)
    birb_group.update()

    screen.blit(ground,(ground_scroll,768))
    if flappy.rect.bottom > 768:
        gameover = True 
        flying = False

    if gameover == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()        
        if event.type == MOUSEBUTTONDOWN and flying == False and gameover == False:
            flying = True
    pygame.display.update()

        

        