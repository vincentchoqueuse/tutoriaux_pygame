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
position_x_mario=400

#BOUCLE INFINIE
continuer = 1

######### Permet de generer plusieurs evenements lorsque l'utilisateur reste appuyer sur une touche
pygame.key.set_repeat(1, 10)

while continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position_x_mario -= 10
            if event.key == pygame.K_RIGHT:
                position_x_mario += 10

    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (position_x_mario,530), (num_image*(mario_width)+80, 0, mario_width, 40))

    pygame.display.flip()
    pygame.time.delay(100)

