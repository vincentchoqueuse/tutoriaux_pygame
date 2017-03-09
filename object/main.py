import pygame
from pygame.locals import *


## definition de l'object Mario (heritage de la classe Sprite)
class Mario(pygame.sprite.Sprite):
    
    num_image=0
    full_image=None
    mario_width=17

    def __init__(self):
        # Constructeur (initialisation de l'objet)
        super().__init__()
        self.full_image = pygame.image.load("mario.png").convert_alpha()
        self.image=self.full_image.subsurface( (self.num_image*self.mario_width+80, 0, self.mario_width, 40))
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=500
    
    def move(self,position):
        #definition de la methode MOVE
        if position=="WAIT":
            self.num_image=0
        if position=="RIGHT":
            self.num_image=1+((self.num_image)%3)  #num image varie de 1 à 4

    def update(self):
        self.image=self.full_image.subsurface( (self.num_image*self.mario_width+80, 0, self.mario_width, 40))
        self.image=pygame.transform.scale(self.image, (34, 80))


## LE PROGRAMME DEBUTE ICI

pygame.init()
pygame.key.set_repeat(1, 10)

fenetre = pygame.display.set_mode((800, 600))
fond = pygame.image.load("background.jpg").convert()

# GESTION DES SPRITES
all_sprites_list = pygame.sprite.Group()
mon_mario = Mario() #on crée un objet mon_mario, definit par la classe Mario.
all_sprites_list.add(mon_mario)

background1_x=0
background2_x=800
continuer = 1
speed=20 #A tester, avec speed=20, il y a un phénomene de repliement du spectre sur le bas de l'image

while continuer:
    
    position="WAIT" # par defaut, Mario reste à sa place
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                position="RIGHT"
                background1_x -= speed
                background2_x -= speed

                if background1_x < -800:
                    background1_x=background1_x+1600
                if background2_x < -800:
                    background2_x=background2_x+1600

    #on appelle la methode de l'objet mon_mario
    mon_mario.move(position)

    # Deux background à la suite
    fenetre.blit(fond, (background1_x,0))
    fenetre.blit(fond, (background2_x,0))

    all_sprites_list.update()
    all_sprites_list.draw(fenetre)

    pygame.display.flip()
    pygame.time.delay(100)

