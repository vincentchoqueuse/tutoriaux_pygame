import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 600))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()

#Chargement et collage du personnage
perso = pygame.image.load("mario.png").convert_alpha()


mario_width=18 # 18 pixels for the mario sprite
num_image=0
background1_x=0
background2_x=800

#BOUCLE INFINIE
continuer = 1

pygame.key.set_repeat(1, 10)

while continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                background1_x -= 10
                background2_x -= 10

                if background1_x < -800:
                    background1_x=background1_x+1600
                if background2_x < -800:
                    background2_x=background2_x+1600


    # Deux background à la suite
    fenetre.blit(fond, (background1_x,0))
    fenetre.blit(fond, (background2_x,0))
    fenetre.blit(perso, (400,530), (num_image*(mario_width)+80, 0, mario_width, 40))

    pygame.display.flip()
    pygame.time.delay(100)

