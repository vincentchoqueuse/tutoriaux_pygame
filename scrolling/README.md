# Tutorial Scrolling

Pour donner un effet de scrolling infini avec le background, il faut coller systématiquement 2 fois le background. Par exemple, si la largeur de la fenêtre est égale à 800, nous utiliserons le code suivant

        background1_x -= 10
        background2_x -= 10

        if background1_x < -800:
            background1_x=background1_x+1600
        if background2_x < -800:
            background2_x=background2_x+1600


        # Deux background à la suite
        fenetre.blit(fond, (background1_x,0))
        fenetre.blit(fond, (background2_x,0))



## Exemple

Le programme main.py montre comment simuler un effet de scrolling
