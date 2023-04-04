import pygame
import random
import sys
from functions import *

pygame.init()

# Set up the Pygame display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)
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
    copy = text(f"Meilleur score : {best_score} | Mohamed Badr Benchekroun",None,30,(255,255,255))
    command = text("Appuyez sur espace",'Start',20,(255,0,0))
    screen.blit(title,((int(screen_width/2-100),int(screen_height/2))))
    screen.blit(copy,((int(screen_width/2-100),int(screen_height/2+50))))
    screen.blit(command,((int(screen_width/2-100),int(screen_height/2+100))))


alien = pygame.image.load("assets/alien.webp")
alien = pygame.transform.scale(alien, (100, 100))
vaisseau = pygame.image.load("assets/vaisseau.png")
lune = pygame.image.load(removebg("assets/moon.png"))
lune = pygame.transform.scale(lune, (screen_width, screen_height))
hole = pygame.image.load(removebg("assets/shadow_ball.png"))
hole = pygame.transform.scale(hole, (80, 80))
rock = pygame.image.load(removebg("assets/stealth_rock.png"))
rock = pygame.transform.scale(rock, (40, 40))
meteor = pygame.image.load(removebg("assets/meteor.png"))
meteor = pygame.transform.scale(meteor, (100, 100))
proj = pygame.image.load(removebg("assets/cross_impact.png"))
proj = pygame.transform.scale(proj, (20, 20))
projalien = pygame.image.load(removebg("assets/explosion_2.png"))
proj = pygame.transform.scale(projalien, (20, 20))

Coordproj = (0,screen_height)
Coordprojalien = (screen_width,0)
Coordhole = (0,screen_height*2)
Coordrock = (0,screen_height)
Coordmeteor = (0,screen_height*1.2)
Coordvaisseau = (screen_width/2,screen_height-96)
Coordalien = (screen_width/2,10)
Coordlune = (-screen_width/1.5,-screen_height/1.5)
right = True
cpt = 0
gameover = 0
game_over = text("GAME OVER","Start",50,(255,0,0))
score = 0
def jeu():
    global Coordvaisseau, Coordalien, right, Coordhole, Coordrock, Coordmeteor, cpt, Coordproj, gameover, score, Coordprojalien
    text_score = text(f"Score : {score}","Start",30,(255,255,255))
    screen.blit(text_score,(0,screen_height/2))
    screen.blit(lune, Coordlune)
    screen.blit(alien, Coordalien)
    screen.blit(vaisseau, Coordvaisseau)
    screen.blit(hole, Coordhole)
    screen.blit(rock, Coordrock)
    screen.blit(meteor, Coordmeteor)
    screen.blit(proj, Coordproj)
    screen.blit(projalien, Coordprojalien)
    cpt+=1
    if cpt>=random.randrange(1,10) & random.randint(1,5)==1:
        if Coordhole[1]>=screen_height:
            Coordhole = (random.randrange(0,screen_width),0)
        Coordhole = (Coordhole[0],Coordhole[1]+2)
    if cpt>=random.randrange(1,10):
        if Coordrock[1]>=screen_height:
            Coordrock = (random.randrange(0,screen_width),0)
        Coordrock = (Coordrock[0],Coordrock[1]+2)
    if cpt>=random.randrange(1,10) & random.randint(1,10)==1:
        if Coordmeteor[1]>=screen_height:
            Coordmeteor = (random.randrange(0,screen_width),0)
    if cpt>=15:
        cpt=0
    if Coordrock[1]<screen_height:
        Coordrock = (Coordrock[0],Coordrock[1]+2)
    if Coordmeteor[1]<screen_height:
        Coordmeteor = (Coordmeteor[0],Coordmeteor[1]+6)
    if Coordhole[1]<screen_height:
        Coordhole = (Coordhole[0],Coordhole[1]+3)
    if right:
        Coordalien = (Coordalien[0] +10, Coordalien[1])
        if Coordalien[0] +10 >= screen_width:
            right = False
    else:
        Coordalien = (Coordalien[0] -10, Coordalien[1])
        if Coordalien[0] -10 <= 0:
            right = True
    if keypress[pygame.K_RIGHT]:
        if Coordvaisseau[0]+ 96 <screen_width:
            Coordvaisseau = ( Coordvaisseau[0] +10 , Coordvaisseau[1] ) 
    if keypress[pygame.K_LEFT]:
        if Coordvaisseau[0]>0:  
            Coordvaisseau = ( Coordvaisseau[0] -10 , Coordvaisseau[1] ) 
    if random.randint(1,50)==3:
        if Coordprojalien==(screen_width,0):
           Coordprojalien=(Coordalien[0]+100/2,100)
        
    if keypress[pygame.K_SPACE]:
            if Coordproj==(0,screen_height):
                Coordproj = (Coordvaisseau[0]+96/2,screen_height-96)
    if Coordvaisseau[1]-Coordhole[1]<2 and Coordvaisseau[0]-Coordhole[0]>-96 and Coordvaisseau[0]-Coordhole[0]<0:
        gameover=1
        print("Fin")
    if Coordvaisseau[1]-Coordrock[1]<2 and Coordvaisseau[0]-Coordrock[0]>-96 and Coordvaisseau[0]-Coordrock[0]<0:
        gameover=1
        print("Fin")
    if Coordvaisseau[1]-Coordmeteor[1]<2 and Coordvaisseau[0]-Coordmeteor[0]>-96 and Coordvaisseau[0]-Coordmeteor[0]<0:
        gameover=1
        print("Fin")
    if Coordvaisseau[1]-Coordprojalien[1]<2 and Coordvaisseau[0]-Coordprojalien[0]>-96 and Coordvaisseau[0]-Coordprojalien[0]<0:
        gameover=1
        print("Fin")
    if Coordproj[1]-Coordalien[1]<2 and Coordproj[0]-Coordalien[0]>-100 and Coordproj[0]-Coordalien[0]<0:
        score+=1
        print(Coordalien,Coordproj)




# Set up the clock
clock = pygame.time.Clock()

# Main game loop
background_y = 0
ingame = 0
while True:
    with open("best_score.txt") as f:
        content=f.read()
    best_score = int(content)
    # Setup
    keypress = pygame.key.get_pressed() 
    clock.tick(60) 
    pygame.display.set_caption(f"Mohamed Badr Benchekroun, 1ere05 | FPS : {round(clock.get_fps(),1)}")
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

            #update coordinates
            lune = pygame.transform.scale(lune, (screen_width, screen_height))
            Coordvaisseau = (screen_width/2,screen_height-96)
            Coordalien = (screen_width/2,10)
            Coordlune = (-screen_width/2,-screen_height/1.5)
            Coordhole = (0,0)
            #adapt
            if ingame:
                jeu()
            else:
                title_screen()
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
    if ingame:
        background_y -=1/2  #vitesse
    else:
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
    
    if Coordproj[1]>=0 and Coordproj!=(0,screen_height):
        Coordproj = (Coordproj[0], Coordproj[1] - 50)
    else:
        Coordproj = (0, screen_height)
    if Coordprojalien[1]>=100:
        print("Launched")
        Coordprojalien = (Coordprojalien[0], Coordprojalien[1] + 30)
    print(Coordprojalien)
    if Coordprojalien[1]>=screen_height:
        print("Arrived")
        Coordprojalien = (screen_width, 0)
    if gameover and ingame:
        screen.blit(game_over,(screen_width/2,screen_width/2))
        pygame.display.update()
        pygame.time.wait(1000)
        gameover=0
        ingame = 0
        pygame.display.update()
        if score > best_score:
            with open("best_score.txt",'w') as f:
                f.write(str(score))
        score = 0
        Coordproj = (0,screen_height)
        Coordprojalien = (screen_width,0)
        Coordhole = (0,screen_height*2)
        Coordrock = (0,screen_height)
        Coordmeteor = (0,screen_height*1.2)
        Coordvaisseau = (screen_width/2,screen_height-96)
        Coordalien = (screen_width/2,10)
        Coordlune = (-screen_width/1.5,-screen_height/1.5)


    # Update the screen, prevents screen tearing and other issues
    pygame.display.update()
