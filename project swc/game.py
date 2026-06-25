import pygame
from character import Character
from boat import Boat
from settings import FONT, SMALL_FONT, BIG_FONT, YELLOW, WHITE, GREEN, RED

class Game:

    def __init__(self, assets):
        self.assets = assets # Simpan assets untuk kegunaan restart
        self.reset_game()

    def reset_game(self):
        # Fungsi ini memudahkan kita untuk panggil semula masa 'Restart'
        self.teacher = Character("Teacher", self.assets["teacher"], 50, 50)
        self.studentA = Character("Student A", self.assets["studentA"], 50, 150)
        self.studentB = Character("Student B", self.assets["studentB"], 50, 250)
        self.supplies = Character("Supplies", self.assets["supplies"], 50, 350)

        self.characters = [
            self.teacher,
            self.studentA,
            self.studentB,
            self.supplies
        ]

        self.boat = Boat(self.assets["boat"])
        
        # Status Game
        self.game_over = False
        self.win = False

    def update(self):
        # Jangan semak peraturan kalau game dah habis
        if self.game_over or self.win:
            return

        # Kemas kini status 'side' setiap watak berdasarkan koordinat X mereka
        for c in self.characters:
            if c.rect.x < 300:
                c.side = "left"
            elif c.rect.x > 550:
                c.side = "right"
            else:
                c.side = "boat" # Watak sedang dalam bot

        # --- LOGIK RULES (PUNCA KALAH) ---
        # 1. Jika Student A bersama Supplies di satu tebing TANPA Teacher, Supplies akan rosak/dimakan!
        if self.studentA.side == self.supplies.side and self.teacher.side != self.studentA.side:
            if self.studentA.side in ["left", "right"]: # Pastikan mereka di tebing, bukan dalam bot
                self.game_over = True

        # 2. Jika Student B bersama Supplies di satu tebing TANPA Teacher
        if self.studentB.side == self.supplies.side and self.teacher.side != self.studentB.side:
            if self.studentB.side in ["left", "right"]:
                self.game_over = True

        # --- LOGIK WIN (PUNCA MENANG) ---
        # Jika semua watak berjaya sampai ke tebing kanan
        if all(c.side == "right" for c in self.characters) and self.boat.side == "right":
            self.win = True

    def draw(self, screen, background):
        screen.blit(background, (0, 0))

        # 1. LUKIS BOT DAHULU (Sebagai Tapak)
        screen.blit(self.boat.image, self.boat.rect)

        # 2. LUKIS WATAK DI ATAS BOT
        for character in self.characters:
            screen.blit(character.image, character.rect)

        # --- Kotak Transparent Untuk RULE (Atas Tengah) ---
        rule_box_width = 700  
        rule_box_x = (800 - rule_box_width) // 2  

        rule_box = pygame.Surface((rule_box_width, 40), pygame.SRCALPHA)
        rule_box.fill((0, 0, 0, 150)) 
        screen.blit(rule_box, (rule_box_x, 15)) 
        
        pygame.draw.rect(screen, WHITE, (rule_box_x, 15, rule_box_width, 40), 2)

        rule_text = SMALL_FONT.render("Rule: Don't leave students with supplies without Teacher!", True, RED)
        screen.blit(rule_text, (rule_box_x + 40, 24))

        # --- Kotak Transparent Untuk GUIDE (Bawah Skrin) ---
        box_width = 640
        box_height = 95
        box_x = (800 - box_width) // 2  
        box_y = 490                      

        guide_box = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        guide_box.fill((0, 0, 0, 150))   
        screen.blit(guide_box, (box_x, box_y))
        
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height), 2)

        title_ins = SMALL_FONT.render("GUIDE:", True, YELLOW)
        line1 = SMALL_FONT.render("[1] Teacher  [2] Student A  [3] Student B  [4] Supplies", True, WHITE)
        
        line2 = SMALL_FONT.render("[SPACEBAR] Move Boat", True, GREEN)
        menu_text = SMALL_FONT.render("          | [M] Main Menu", True, GREEN) 

        text_padding_x = box_x + 20
        screen.blit(title_ins, (text_padding_x, box_y + 10))
        screen.blit(line1, (text_padding_x, box_y + 38))
        
        screen.blit(line2, (text_padding_x, box_y + 65))
        screen.blit(menu_text, (text_padding_x + 180, box_y + 65))

        # --- PAPARAN SKRIN KALAH / MENANG (BUTANG MENU DIKEMASKINI) ---
        if self.game_over:
            overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180)) 
            screen.blit(overlay, (0, 0))
            
            go_text = BIG_FONT.render("GAME OVER", True, RED)
            res_text = FONT.render("Press 'R' to Restart  |  'M' for Menu", True, WHITE)
            exit_text = SMALL_FONT.render("Press 'ESC' to Exit", True, RED)
            
            screen.blit(go_text, (250, 200))
            screen.blit(res_text, (200, 300))
            screen.blit(exit_text, (330, 360))

        elif self.win:
            overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            win_text = BIG_FONT.render("YOU WIN!", True, GREEN)
            res_text = FONT.render("Press 'R' to Play Again  |  'M' for Menu", True, WHITE)
            exit_text = SMALL_FONT.render("Press 'ESC' to Exit", True, RED)
            
            screen.blit(win_text, (290, 200))
            screen.blit(res_text, (200, 300))
            screen.blit(exit_text, (330, 360))

    def toggle_character(self, character):
        if self.game_over or self.win: return 
        
        if not hasattr(character, "in_boat"):
            character.in_boat = False

        if not character.in_boat:
            passengers = sum(1 for c in self.characters if getattr(c, 'in_boat', False))
            if passengers >= 2: return 

            slot_offset = 20 if passengers == 0 else 80
            character.rect.x = self.boat.rect.x + slot_offset
            character.rect.y = self.boat.rect.y + 5
            character.in_boat = True
        else:
            if self.boat.side == "left":
                character.rect.x = 50
            else:
                character.rect.x = 700
            
            if character.name == "Teacher": character.rect.y = 50
            elif character.name == "Student A": character.rect.y = 150
            elif character.name == "Student B": character.rect.y = 250
            elif character.name == "Supplies": character.rect.y = 350
            
            character.in_boat = False

    def move_boat_with_passengers(self):
        if self.game_over or self.win: 
            return

        if not self.teacher.in_boat:
            return 

        self.boat.move()

        passengers_found = 0
        for character in self.characters:
            if getattr(character, "in_boat", False):
                slot_offset = 20 if passengers_found == 0 else 80
                character.rect.x = self.boat.rect.x + slot_offset
                passengers_found += 1