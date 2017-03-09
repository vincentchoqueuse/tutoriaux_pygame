# Tutorial Programmation orientée Objet

La programmation de jeux vidéos se fait le plus souvent non pas en adoptant une programmation procédurale classique mais en adoptant une approche orientée objet.

Concretement, cela revient à définir de "grosses structures", appelées *Classes*, avec ses propriétés et ses fonctions associées, appelées *Methodes*. Par exemple, pour programmer un jeu similaire à Mario Bros, nous pouvons définir une classe Mario avec ses methodes specifiques: initialiser Mario, bouger Mario, afficher Mario, etc.

Cette approche orientée "objet" "possède deux avantages majeurs. 

* D'une part, le code est plus propre car les methodes associées à un objet sont définies avec l'objet. 
* D'autre part, il est possible de mettre en oeuvre un mécanisme d'héritage. Par exemple, nous pouvons tout d'abord définir une classe générale Personnage avec ses methodes *bouger* et *afficher*. Puis dans un second temps, nous pouvons créer une sous-classe Mario héritant des methodes de la classe mère Personnage. Dans ce cas, plus besoin de rédéfinir les méthodes *bouger* et *afficher*, le classe Mario heritera des methodes de la classe Personnage.

    
Sous Pygame, la classe Personnage s'appelle *Sprite*. La classe Sprite possède un certain nombre de méthodes pour l'affichage, la détection de collision des personnages etc etc. Pour définir une classe héritée, il suffit de définir le code suivant: 


        class Mario(pygame.sprite.Sprite):

            #Mes propriétés       
            full_image=None
            mario_width=17

            def __init__(self):
                # Constructeur (initialisation de l'objet)
                super().__init__()
                self.full_image = pygame.image.load("mario.png").convert_alpha()
                self.image=self.full_image.subsurface( (80, 0, self.mario_width, 40))
                self.rect = self.image.get_rect()
                self.rect.x=400
                self.rect.y=500

            def update(self):
                self.image=self.full_image.subsurface( (80, 0, self.mario_width, 40))
                self.image=pygame.transform.scale(self.image, (34, 80))



## Exemple

Le programme main.py montre comment utiliser la classe Sprite pour gérer les mouvements de Mario.
