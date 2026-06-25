import pygame
from settings import *

def show_menu(screen, background):

    while True:

        screen.blit(background, (0,0))

        title = BIG_FONT.render(
            "School Field Trip",
            True,
            BLACK
        )

        start = FONT.render(
            "Press ENTER To Start",
            True,
            YELLOW
        )

        quit_text = FONT.render(
            "ESC To Exit",
            True,
            RED
        )

        screen.blit(title, (280, 180))
        screen.blit(start, (350, 300))
        screen.blit(quit_text, (390, 360))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return True

                if event.key == pygame.K_ESCAPE:
                    return False