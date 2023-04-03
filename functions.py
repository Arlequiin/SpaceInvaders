import pygame
from PIL import Image

def removebg(path):
    im = Image.open(path)
    im = im.convert('RGBA')
    pixels = im.load()
    width, height = im.size
    t=pixels[0,0]
    for j in range(height):
        for i in range(width):
            if t[0]+30>pixels[i,j][0]>t[0]-30 and t[1]+30>pixels[i,j][1]>t[1]-30 and t[2]+30>pixels[i,j][2]>t[2]-30:
                pixels[i,j]=(0,0,0,0)
    im.save(path)
    return path

def text(words, fnt="Arial", size=20, color=(255,255,255)):
    if fnt=="Start":
        fnt="assets/PressStart2p-Regular.ttf"
    font = pygame.font.SysFont(fnt, size)
    txt = font.render(words, 1, color)
    return txt
