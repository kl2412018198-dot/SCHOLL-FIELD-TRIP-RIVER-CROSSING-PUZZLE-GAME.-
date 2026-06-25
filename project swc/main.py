import pygame
import sys

from sound_manager import SoundManager
from settings import *
from menu import show_menu
from game import Game

pygame.init()
pygame.mixer.init()

sound_manager = SoundManager()
sound_manager.play_bg()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "School Field Trip"
)

background = pygame.image.load(
    "assets/images/background.png"
)
background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

assets = {

    "teacher":
    pygame.transform.scale(
        pygame.image.load(
            "assets/images/teacher.png"
        ),
        (80,80)
    ),

    "studentA":
    pygame.transform.scale(
        pygame.image.load(
            "assets/images/studentA.png"
        ),
        (80,80)
    ),

    "studentB":
    pygame.transform.scale(
        pygame.image.load(
            "assets/images/studentB.png"
        ),
        (80,80)
    ),

    "supplies":
    pygame.transform.scale(
        pygame.image.load(
            "assets/images/supplies.png"
        ),
        (80,80)
    ),

    "boat":
    pygame.transform.scale(
        pygame.image.load(
            "assets/images/boat.png"
        ),
        (150,80)
    )
}

start = show_menu(
    screen,
    background
)

if not start:
    pygame.quit()
    sys.exit()

game = Game(assets)

clock = pygame.time.Clock()

running = True

# --- TAMBAH FUNGSI INI DI ATAS WHILE RUNNING (Jika belum ada) ---
def go_to_menu():
    global running
    start = show_menu(screen, background)
    if not start:
        return False
    else:
        game.reset_game() # Reset game supaya posisi watak kembali ke asal
        return True

# --- KEMAS KINI LOOP UTAMA ---
while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # HANYA KESAN KEYBOARD SAHAJA
        if event.type == pygame.KEYDOWN:

            sound_manager.play_click()
            
            # Tekan M untuk kembali ke Menu
            if event.key == pygame.K_m:
                if not go_to_menu():
                    running = False

            # Tekan R untuk Restart game
            elif event.key == pygame.K_r:
                game.reset_game()
                
            # Tekan ESC untuk keluar game
            elif event.key == pygame.K_ESCAPE:
                running = False

            # Input Kawalan Watak & Bot
            elif event.key == pygame.K_1: game.toggle_character(game.teacher)
            elif event.key == pygame.K_2: game.toggle_character(game.studentA)
            elif event.key == pygame.K_3: game.toggle_character(game.studentB)
            elif event.key == pygame.K_4: game.toggle_character(game.supplies)
            elif event.key == pygame.K_SPACE: game.move_boat_with_passengers()

    game.update()
    game.draw(screen, background)
    pygame.display.update()

pygame.quit()