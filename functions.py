import pygame
from PIL import Image
import os

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
    font = pygame.font.SysFont(fnt, size)
    txt = font.render(words, 1, color)
    return txt

def extract_square_frames(image_path):
    img = Image.open(image_path)
    width, height = img.size
    n_frames = height // width
    frames_dir = os.path.splitext(image_path)[0]
    os.makedirs(frames_dir, exist_ok=True)
    for i in range(n_frames):
        frame = img.crop((0, i*width, width, (i+1)*width))
        frame.save(os.path.join(frames_dir, f"{i}.png"))

extract_square_frames("assets/explosion_4.png")