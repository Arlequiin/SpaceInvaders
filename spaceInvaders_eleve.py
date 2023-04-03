## -*- coding: utf-8 -*-

import pygame  
import time

pygame.init() # initialisation du module "pygame" 
fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Mohamed Badr Benchekroun, 1ere05") # Définit le titre de la fenêtre

def text(words, fnt="Arial", size=20, color=(255,255,255)):
    if fnt=="Start":
        fnt="assets/PressStart2p-Regular.ttf"
    font = pygame.font.SysFont(fnt, size)
    txt = font.render(words, 1, color)
    return txt

imageAlien = pygame.image.load("assets/alien.png")
imageVaisseau = pygame.image.load("assets/vaisseau.png")


# update the display
pygame.display.flip()

# update the display
pygame.display.flip()
imageVaisseau = pygame.transform.scale(imageVaisseau, (64, 64)) # On redimensionne l'image du vaisseau à une taille de 64x64 pixels

# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionVaisseau = (300,525)
positionAlien = (300,10)
projectile = (-1, -1)


# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner(score,proj):
    global imageAlien, imageVaisseau, fenetre, projectile
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenêtre avant de la dessiner
    fenetre.fill( (0,0,0) )
    font = pygame.font.Font('assets/PressStart2P-Regular.ttf', 10)
    text_score = font.render(f'Score : {score}', True, (255, 255, 255))
    text_missiles = font.render(f'Projectiles restants : {proj}', True, (255, 255, 255))
    fenetre.blit(text_score, (0, 100))
    fenetre.blit(text_missiles, (0, 120))
    fenetre.blit(imageVaisseau, positionVaisseau) # On dessine l'image du vaisseau à sa position
    fenetre.blit(imageAlien, positionAlien)  # On dessine l'image du vaisseau à sa position
    if projectile != (-1, -1):
        pygame.draw.circle(fenetre, (255,255,255), projectile, 5) # On dessine le projectile (un simple petit cercle)
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
def gererClavierEtSouris():
    global continuer, positionVaisseau, projectile
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier: Quelles touches sont pressées ?
    touchesPressees = pygame.key.get_pressed() 
    font = pygame.font.Font(None, 50)
    text_game_over = font.render(f'GAME OVER!', True, (255, 0, 0))
    if touchesPressees[pygame.K_SPACE]:
        if proj>0:
          projectile = (positionVaisseau[0]+64/2,positionVaisseau[1])
        else:
            fenetre.blit(text_game_over, (200, 220))
    if touchesPressees[pygame.K_RIGHT]:
        if positionVaisseau[0]+ 64 <screen_info.current_w:
            positionVaisseau = ( positionVaisseau[0] + 5 , positionVaisseau[1] )
    if touchesPressees[pygame.K_LEFT]:
        if positionVaisseau[0]>0:  
            positionVaisseau = ( positionVaisseau[0] - 5 , positionVaisseau[1] )


# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
score = 0
proj = 10
while continuer==1:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(100) 
    pygame.display.set_caption(f"Mohamed Badr Benchekroun, 1ere05 | FPS : {clock.get_fps()}")
    dessiner(score,proj)
    gererClavierEtSouris()

    # On fait avancer le projectile (si il existe)
    if proj>0:
        if projectile != (-1, -1) and projectile[1]>50:
            projectile = (projectile[0], projectile[1] - 10)
        if projectile[1]==45:
            proj-=1
            if projectile[0]==positionVaisseau[0]:
                proj-=1
            diff = (projectile[0]-positionAlien[0])
            if diff<45 and diff > -1:
                pygame.draw.circle(fenetre, (255,0,0), projectile, 20)
                pygame.draw.circle(fenetre, (255, 69, 0), projectile, 15)
                pygame.draw.circle(fenetre, (255, 165, 0), projectile, 5)
                time.sleep(1)
                positionAlien=(-2, -2)
            projectile=(-1,-1)
        pygame.display.flip()



## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
