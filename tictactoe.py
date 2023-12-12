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

plateau = np.zeros((lignes_plateau, colonnes_plateau))


def lignes():
    pygame.draw.line(fenetre, WHITE, (0, 270), (800, 270), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (0, 600), (800, 600), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (270, 0), (270, 800), largeur_ligne)
    pygame.draw.line(fenetre, WHITE, (600, 0), (600, 800), largeur_ligne)


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


def carre_occupe(ligne, colonne, joueur):
    plateau[ligne][colonne] = joueur


def carre_libre(ligne, colonne):
    return plateau[ligne][colonne] == 0


def plateau_rempli():
    for ligne in range(lignes_plateau):
        for colonne in range(colonnes_plateau):
            if plateau[ligne][colonne] == 0:
                return False
    return True


def victoire(player):
    for colonne in range(colonnes_plateau):
        if plateau[0][colonne] == player and plateau[2][colonne] == player:
            victoire_verticale(colonne, player)
            return True

    for ligne in range(lignes_plateau):
        if plateau[ligne][0] == player and plateau[ligne][1] == player and plateau[ligne][2] == player:
            victoire_horizontale(ligne, player)
            return True

    if plateau[2][0] == player and plateau[1][1] == player and plateau[0][2] == player:
        diagonale1(player)
        return True

    if plateau[0][0] == player and plateau[1][1] == player and plateau[2][2] == player:
        diagonale2(player)
        return True

    return False


def victoire_verticale(colonne, player):
    posX = colonne * 270 + 100
    if player == 1:
        color = WHITE
    elif player == 2:
        color = WHITE

    pygame.draw.line(fenetre, WHITE, (posX, 15), (posX, HEIGHT - 15), 15)


def victoire_horizontale(ligne, player):
    posY = ligne * 270 + 100

    if player == 1:
        color = WHITE
    elif player == 2:
        color = WHITE

    pygame.draw.line(fenetre, WHITE, (15, posY), (WIDTH - 15, posY), 15)


def diagonale1(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = WHITE

    pygame.draw.line(fenetre, WHITE, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def diagonale2(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = WHITE

    pygame.draw.line(fenetre, WHITE, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


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
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            ligne_cliquee = int(mouseY // 266)
            colonne_cliquee = int(mouseX // 266)

            if carre_libre(ligne_cliquee, colonne_cliquee):
                if player == 1:
                    carre_occupe(ligne_cliquee, colonne_cliquee, 1)
                    if victoire(player):
                        restart()
                    player = 2

                elif player == 2:
                    carre_occupe(ligne_cliquee, colonne_cliquee, 2)
                    if victoire(player):
                        restart()
                    player = 1

                dessinrond()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()


    
   
            