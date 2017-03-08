# Tutorial Event

La lecture du claver s'obtient en utilisant la fonction get() du module event. Plus précisement, il faudra procéder de la manière suivante

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 10
                if event.key == pygame.K_RIGHT:
                    x += 10

Ainsi, lorsque le joueur appuie sur la flèche de gauche, la variable x sera décrementée de 10. A l'opposé, si le joueur appuie sur la flèche de droite, la variable x sera incrémentée de 10.


## Exemple

Le programme main.py montre comment déplacer horizontalement mario à partir du clavier.
