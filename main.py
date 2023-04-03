import pygame
import random
import sys
from functions import *

pygame.init()

# Set up the Pygame display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("SPACE INVADER - Badr 1ère05 | FPS : ")

# Pre-render the background image
background_img = pygame.Surface((screen_width, screen_height))
for y in range(screen_height):
    for x in range(screen_width):
        temp = random.choice([True]+[False]*600) #frequence etoiles = 1/n
        if temp:
            color = (255, 255, 255)
        else:
            color = (0,0,random.randrange(0,50))
        background_img.set_at((x, y), color)

# Function to draw the background
def draw_background():
    global background_y
    screen.blit(background_img, (0, background_y))
    screen.blit(background_img, (0, background_y+screen_height))

def title_screen():
    title = text("SPACE INVADER","Start",50,(0,255,0))
    copy = text("Mohamed Badr Benchekroun",None,30,(255,255,255))
    command = text("Appuyez sur espace",'Start',20,(255,0,0))
    screen.blit(title,((int(screen_width/2-100),int(screen_height/2))))
    screen.blit(copy,((int(screen_width/2-100),int(screen_height/2+50))))
    screen.blit(command,((int(screen_width/2-100),int(screen_height/2+100))))


alien = pygame.image.load("assets/alien.png")
vaisseau = pygame.image.load("assets/vaisseau.png")
lune = pygame.image.load(removebg("assets/moon.png"))
lune = pygame.transform.scale(lune, (screen_height, screen_width))
Coordvaisseau = (screen_width/2,screen_height-96)
Coordalien = (screen_width/2,10)
Coordlune = (-screen_width/2,-screen_height/1.5)
def jeu():
    global Coordvaisseau, Coordalien
    screen.blit(vaisseau, Coordvaisseau)
    screen.blit(alien, Coordalien)
    screen.blit(lune, Coordlune)
    right = True
    if right:
        Coordalien = (Coordalien[0] + 5, Coordalien[1])
        if Coordalien[0] + 5 >= screen_width:
            right = False
    else:
        Coordalien = (Coordalien[0] - 5, Coordalien[1])
        if Coordalien[0] - 5 <= 0:
            right = True
    if keypress[pygame.K_RIGHT]:
        if Coordvaisseau[0]+ 96 <screen_width:
            Coordvaisseau = ( Coordvaisseau[0] + 5 , Coordvaisseau[1] ) 
    if keypress[pygame.K_LEFT]:
        if Coordvaisseau[0]>0:  
            Coordvaisseau = ( Coordvaisseau[0] - 5 , Coordvaisseau[1] ) 


# Set up the clock
clock = pygame.time.Clock()

# Main game loop
background_y = 0
ingame = 0
while True:
    # Setup
    keypress = pygame.key.get_pressed() 
    clock.tick(100) 
    pygame.display.set_caption(f"Mohamed Badr Benchekroun, 1ere05 | FPS : {round(clock.get_fps(),1)}")
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size
            if ingame:
                jeu()
            else:
                title_screen()
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            # Update the background
            background_img = pygame.Surface((screen_width, screen_height))
            for y in range(screen_height):
                for x in range(screen_width):
                    temp = random.choice([True]+[False]*600)
                    if temp:
                        color = (255, 255, 255)
                    else:
                        color = (0,0,random.randrange(0,50))
                    background_img.set_at((x, y), color)

    # Animation fond
    background_y -= 1/5 #vitesse
    if background_y < -screen_width:
        background_y = 0

    # Draw the background
    draw_background()
    if ingame:
        jeu()
    else:
        title_screen()
        if keypress[pygame.K_SPACE]:
            ingame = 1
    # Update the screen
    pygame.display.update()
