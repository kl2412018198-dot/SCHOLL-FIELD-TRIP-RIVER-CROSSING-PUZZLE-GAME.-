import pygame
def draw_text(screen,text,font,color,x,y):
    screen.blit(font.render(text,True,color),(x,y))