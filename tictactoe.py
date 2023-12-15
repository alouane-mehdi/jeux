import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
radius_cercle = 55
largeur_cercle = 15
largeur_ligne = 10
largeur_croix = 20
espace = 50
lignes_plateau = 3
colonnes_plateau = 3

fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
fenetre.fill(BLACK)

# Représentation de la grille
plateau = np.zeros((lignes_plateau, colonnes_plateau))

# Liste pour stocker les coordonnées des coups
coups = []

# Fonction pour dessiner les lignes de la grille
def lignes():
    pygame.draw.line(fenetre, WHITE, (0, 270), (800, 270), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (0, 600), (800, 600), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (270, 0), (270, 800), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (600, 0), (600, 800), largeur_ligne)

# Fonction pour dessiner les ronds et croix
def dessinrond():
    for ligne in range(lignes_plateau):
        for colonne in range(colonnes_plateau):
            if plateau[ligne][colonne] == 1:
                pygame.draw.circle(fenetre, WHITE, (int(colonne * 270 + 133), int(ligne * 270 + 133)),
                                   radius_cercle, largeur_cercle)
            elif plateau[ligne][colonne] == 2:
                pygame.draw.line(fenetre, WHITE, (colonne * 270 + espace, ligne * 270 + 270 - espace),
                                 (colonne * 270 + 270, ligne * 270 - espace), largeur_croix)
                pygame.draw.line(fenetre, WHITE, (colonne * 270 + espace, ligne * 270 + espace),
                                 (colonne * 270 + 270, ligne * 270 + 270 - espace), largeur_croix)

# Fonction pour marquer que la case est occupée par un joueur
def carre_occupe(ligne, colonne, joueur):
    plateau[ligne][colonne] = joueur

# Fonction pour vérifier si la case est libre
def carre_libre(ligne, colonne):
    return plateau[ligne][colonne] == 0


# Fonction pour vérifier s'il y a une victoire
def victoire(player):
    for ligne in range(lignes_plateau):
        if all(plateau[ligne][colonne] == player for colonne in range(colonnes_plateau)):
            victoire_horizontale(ligne, player)
            print("Victoire !")
            return True

    for colonne in range(colonnes_plateau):
        if all(plateau[ligne][colonne] == player for ligne in range(lignes_plateau)):
            victoire_verticale(colonne, player)
            print("Victoire !")
            return True

    if all(plateau[ligne][colonne] == player for ligne in range(lignes_plateau)):
        diagonale1(player)
        print("Victoire !")
        return True

    if all(plateau[ligne][lignes_plateau - ligne - 1] == player for ligne in range(lignes_plateau)):
        diagonale2(player)
        print("Victoire !")
        return True

    return False


# Fonction pour dessiner la ligne verticale en cas de victoire
def victoire_verticale(colonne, player):
    posX = colonne * 270 + 100
    pygame.draw.line(fenetre, WHITE, (posX, 15), (posX, HEIGHT - 15), 15)

# Fonction pour dessiner la ligne horizontale en cas de victoire
def victoire_horizontale(ligne, player):
    posY = ligne * 270 + 100
    pygame.draw.line(fenetre, WHITE, (15, posY), (WIDTH - 15, posY), 15)

# Fonction pour dessiner la première diagonale en cas de victoire
def diagonale1(player):
    pygame.draw.line(fenetre, WHITE, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

# Fonction pour dessiner la deuxième diagonale en cas de victoire
def diagonale2(player):
    pygame.draw.line(fenetre, WHITE, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

# Fonction pour redémarrer le jeu
def restart():
    fenetre.fill(BLACK)
    lignes()
    player = 1
    for ligne in range(lignes_plateau):
        for colonne in range(colonnes_plateau):
            plateau[ligne][colonne] = 0



lignes()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            ligne_cliquee = int(mouseY // (HEIGHT / lignes_plateau))
            colonne_cliquee = int(mouseX // (WIDTH / colonnes_plateau))

            if carre_libre(ligne_cliquee, colonne_cliquee):
                coups.append((ligne_cliquee, colonne_cliquee))
                print("Coordonnées des coups :", coups)
                    # Afficher les coordonnées des coups


                if player == 1:
                    carre_occupe(ligne_cliquee, colonne_cliquee, 1)
                    if victoire(player):
                        print(player, "player")
                        
                    player = 2

                elif player == 2:
                    carre_occupe(ligne_cliquee, colonne_cliquee, 2)
                    if victoire(player):
                        print(player, "player 2")
                        
                    player = 1

                dessinrond()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
        
    
    
    pygame.display.flip()




   
            