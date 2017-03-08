import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 600))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("mario.png").convert_alpha()


mario_width=18 # 18 pixels for the mario sprite
num_image=0
fenetre.blit(perso, (400,530), (num_image*(mario_width)+80, 0, mario_width, 40))


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    continuer = int(input())
