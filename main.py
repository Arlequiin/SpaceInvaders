import pygame
import random
import sys
from functions import *

pygame.init()

# Set up the Pygame display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF|pygame.HWSURFACE|pygame.RESIZABLE)
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
    title = text("SPACE INVADER",'assets/PressStart2p-Regular.ttf',50,(0,255,0))
    copy = text(f"Meilleur score : {best_score} | Mohamed Badr Benchekroun",None,30,(255,255,255))
    command = text("Appuyez sur espace",'assets/PressStart2p-Regular.ttf',20,(255,0,0))
    summary = text("Vous êtes un astronaute de l'équipage du vaisseau SpaceY. De nombreuses météorites et trous noirs",'assets/PressStart2p-Regular.ttf',20,(255,255,255))
    summary2 = text("ont fait leur apparition à proximité de la Lune, le Professeur Einstein IV pense que cela est du à la présence d'extraterrestres, ",'assets/PressStart2p-Regular.ttf',20,(255,255,255))
    summary3 = text("leurs vaisseaux fonctionnant à l'énergie noire. Votre mission est d'abattre un maximum de ces vaisseaux.",'assets/PressStart2p-Regular.ttf',20,(255,255,255))   
    screen.blit(title,((screen_width//2-100,screen_height//2)))
    screen.blit(copy,(screen_width//2-100,screen_height//2+50))
    screen.blit(command,(((screen_width//2-100),screen_height//2+100)))
    screen.blit(summary,(0,screen_height//2+200))
    screen.blit(summary2,(0,screen_height//2+230))
    screen.blit(summary3,(0,screen_height//2+250))

bottle = pygame.image.load("assets/alien.webp")
Coordbottle = (0,screen_height)
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
meteor = pygame.transform.rotate(meteor, 210)
proj = pygame.image.load(removebg("assets/cross_impact.png"))
projalien = pygame.image.load(removebg("assets/explosion_2.png"))
explosion = []
Coordexplosion = []
for i in range(4):
    explosion.append(pygame.image.load(removebg(f"assets/explosion_4/{i}.png")))
    explosion[i] = pygame.transform.scale(explosion[i], (100, 100))
    Coordexplosion.append((0,screen_height))
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
life = 5
projectiles_restants = 100
game_over = text("GAME OVER",'assets/PressStart2p-Regular.ttf',50,(255,0,0))
score = 0
def jeu():
    global Coordvaisseau, Coordalien, right, Coordhole, Coordrock, Coordmeteor, cpt, Coordproj, gameover, score, Coordprojalien, explosion, Coordexplosion, Coordlune, bottle, Coordbottle, life, projectiles_restants
    text_score = text(f"Score : {score}",'assets/PressStart2p-Regular.ttf',30,(255,0,0))
    text_life = text(f"Score : {life*'•'}",'assets/PressStart2p-Regular.ttf',30,(255,0,0))
    text_proj = text(f"Projectiles : {projectiles_restants}",'assets/PressStart2p-Regular.ttf',30,(255,0,0))
    screen.blit(lune, Coordlune)
    screen.blit(alien, Coordalien)
    screen.blit(vaisseau, Coordvaisseau)
    screen.blit(hole, Coordhole)
    screen.blit(rock, Coordrock)
    screen.blit(meteor, Coordmeteor)
    screen.blit(bottle, Coordbottle)
    screen.blit(proj, Coordproj)
    screen.blit(projalien, Coordprojalien)
    screen.blit(text_score,(0,screen_height/2))
    screen.blit(text_life,(0,screen_height/2+20))
    screen.blit(text_proj,(0,screen_height/2+40))
    for i in range(4):
        screen.blit(explosion[i], Coordexplosion[i])
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
    if cpt>=random.randrange(1,10) & random.randint(1,20)==1:
        if Coordbottle[1]>=screen_height:
            Coordbottle = (random.randrange(0,screen_width),0)
    if cpt>=15:
        cpt=0
    if Coordrock[1]<screen_height:
        Coordrock = (Coordrock[0],Coordrock[1]+2)
    if Coordmeteor[1]<screen_height:
        Coordmeteor = (Coordmeteor[0],Coordmeteor[1]+6)
    if Coordhole[1]<screen_height:
        Coordhole = (Coordhole[0],Coordhole[1]+3)
    if Coordbottle[1]<screen_height:
        Coordbottle = (Coordbottle[0],Coordbottle[1]+1)
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
    if random.randint(1,100)==3:
        if Coordprojalien==(screen_width,0):
           Coordprojalien=(Coordalien[0]+100/2,100)
        
    if keypress[pygame.K_SPACE]:
            if projectiles_restants>0:
                if Coordproj==(0,screen_height):
                    Coordproj = (Coordvaisseau[0]+96/2,screen_height-96)
                projectiles_restants-=1
    if Coordvaisseau[1]-Coordhole[1]<2 and Coordvaisseau[0]-Coordhole[0]>-96+96/2 and Coordvaisseau[0]-Coordhole[0]<+96/2:
        life-=1
    if Coordvaisseau[1]-Coordrock[1]<2 and Coordvaisseau[0]-Coordrock[0]>-96+96/2 and Coordvaisseau[0]-Coordrock[0]<+96/2:
        life-=1
    if Coordvaisseau[1]-Coordmeteor[1]<2 and Coordvaisseau[0]-Coordmeteor[0]>-96+96/2 and Coordvaisseau[0]-Coordmeteor[0]<+96/2:
        life-=1
    if Coordvaisseau[1]-Coordprojalien[1]<2 and Coordvaisseau[0]-Coordprojalien[0]>-96+96/2 and Coordvaisseau[0]-Coordprojalien[0]<+96/2:
        life-=1
    if Coordvaisseau[1]-Coordbottle[1]<2 and Coordvaisseau[0]-Coordbottle[0]>-96+96/2 and Coordvaisseau[0]-Coordbottle[0]<+96/2:
        projectiles_restants+=1
    if Coordproj[1]-Coordalien[1]<2 and Coordproj[0]-Coordalien[0]>-50 and Coordproj[0]-Coordalien[0]<50:
        score+=1
        for i in range(4):
            Exp_frame=explosion[i]
            screen.blit(Exp_frame,Coordalien)
            pygame.display.flip()
            pygame.time.wait(100)
            Coordexplosion[i]=(0,screen_height)
            Coordlune=(Coordlune[0],Coordlune[1]+5)
        Coordalien=(-1,-1)




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
            Coordprojalien = (screen_width,0)
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
                    temp = random.choice([True]+[False]*100) #frequence of stars
                    if temp:
                        color = (255, 255, 255)
                    else:
                        color = (0,0,random.randrange(0,50))
                    background_img.set_at((x, y), color)

    # Animation fond
    if ingame:
        background_y -=1/5  #vitesse
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
        Coordproj = (Coordproj[0], Coordproj[1] - 70)
    else:
        Coordproj = (0, screen_height)
    if Coordprojalien[1]>=100:
        Coordprojalien = (Coordprojalien[0], Coordprojalien[1] + 30)
    if Coordprojalien[1]>=screen_height:
        Coordprojalien = (screen_width, 0)
    if life==0:
        gameover=1
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
