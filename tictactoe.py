import pygame
import sys
import numpy as np

pygame.init()

WIDTH= 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
radius_cercle= 60
largeur_cercle= 15
largeur_ligne = 15
largeur_croix = 30
espace = 80
lignes_plateau = 3
colonnes_plateau = 3

fenetre= pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
fenetre.fill( BLACK )


plateau = np.zeros( (lignes_plateau, colonnes_plateau) )




def lignes():
    pygame.draw.line(fenetre, WHITE, (0, 266), (800, 266), largeur_ligne )
    pygame.draw.line(fenetre, WHITE, (0, 600), (800, 600), largeur_ligne )
    pygame.draw.line(fenetre, WHITE, (266, 0), (266, 800), largeur_ligne )
    pygame.draw.line(fenetre, WHITE, (600, 0), (600, 800), largeur_ligne )
    
def dessinrond():
    for ligne in range(lignes_plateau):
        for colonne in range(colonnes_plateau):
            if plateau[ligne][colonne] == 1:
                pygame.draw.circle(fenetre, WHITE, (int(colonne * 270 + 133), int( ligne * 270 + 133 )), radius_cercle, largeur_cercle )
            elif plateau[ligne][colonne]==2:
                pygame.draw.line(fenetre, WHITE, (colonne * 270 + espace, ligne * 270 + 270-espace), (colonne * 270 + 270, ligne * 270-espace), largeur_croix)
                pygame.draw.line(fenetre, WHITE, (colonne * 270 + espace, ligne * 270 + espace ),(colonne * 270 + 270 , ligne * 270 + 270 - espace), largeur_croix)
                    

def carre_occupe(ligne, colonne, joueur):
    plateau[ligne][colonne] = joueur
    
def carre_libre(ligne, colonne):
    if plateau[ligne][colonne] == 0:
        return True  
    else:
        return False  
    
def plateau_rempli():
    for ligne in range(lignes_plateau):
        for colonne in range(colonnes_plateau):
            if plateau[ligne][colonne]==0:
                return False
            
    return True


lignes()

player = 1     

while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y
            
            ligne_cliquee= int(mouseY // 266)
            colonne_cliquee = int(mouseX // 266)
            
            
            if carre_libre ( ligne_cliquee, colonne_cliquee) :
                if player == 1:
                    carre_occupe( ligne_cliquee, colonne_cliquee, 1)
                    player = 2
                    
                elif player == 2:
                    carre_occupe( ligne_cliquee, colonne_cliquee, 2)
                    player = 1
                    
                
                dessinrond()    
                
                    
                    
                        
                
            
        
    
    pygame.display.update()


    
   
            