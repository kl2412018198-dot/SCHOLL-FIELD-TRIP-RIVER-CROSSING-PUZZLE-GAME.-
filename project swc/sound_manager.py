import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init() # Pastikan mixer diaktifkan
        try:
            self.click = pygame.mixer.Sound('assets/sounds/click.wav')
            self.bg_music = pygame.mixer.Sound('assets/sounds/bg_music.wav')
        except Exception as e:
            print(f"Amaran: Fail bunyi tidak dijumpai! {e}")
            self.click = None
            self.bg_music = None

    def play_click(self):
        if self.click:
            self.click.play()

    def play_bg(self):
        if self.bg_music:
            # loops=-1 supaya lagu latar bermain berulang-ulang tanpa henti
            self.bg_music.play(loops=-1) 
            
    def stop_bg(self):
        if self.bg_music:
            self.bg_music.stop()