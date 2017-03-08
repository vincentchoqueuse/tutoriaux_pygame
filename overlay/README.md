# Tutorial Overlay

Pour ajouter une image sur la fenêtre principale, il faut:

* Ouvrir la fenetre principale: `pygame.display.set_mode((800, 600))`
* Charger une image dans une variable: `fond = pygame.image.load("background.jpg").convert()`
* Coller l'image sur la fenêtre principale au moyen de la fonction blit: `fenetre.blit(fond, (0,0))`

Pour superposer différentes images (fond + sprite par exemple), faites très attention à l'ordre dans lequel vous allez coller les images. Il faut tout d'abord coller l'image de fond puis coller le sprite sur le plan supérieur.

## Exemple

Le programme main.py montre comment charger une image de fond ainsi que le personnage Mario. Remarquons que le personnage Mario est stocké dans l'image mario.png. Cette image contient différentes images de mario (immobile, en train de sauter, etc). Il est possible de coller une partie particulière de l'image en ajoutant un troisième argument à la fonction blit.

        mario_width=18 # 18 pixels for the mario sprite
        num_image=0
        fenetre.blit(perso, (400,530), (num_image*(mario_width)+80, 0, mario_width, 40))

