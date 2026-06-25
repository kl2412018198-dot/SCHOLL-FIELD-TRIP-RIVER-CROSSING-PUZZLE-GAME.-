import pygame

class Character:

    def __init__(self, name, image, x, y):
        self.name = name
        self.image = image
        self.side = "left"
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)