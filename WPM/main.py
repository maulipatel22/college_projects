import pygame
from pygame.locals import *
import sys
import GalaxyShoot
import WPM

class KeyboardNinja():
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.MAIN_C = (255, 127, 0)
        self.WHITE = (255, 255, 255)

        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Keyboard Ninja')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.WIDTH / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()


    def run_game(self):
        self.is_running = True
        while self.is_running:
            self.draw_text(self.screen, "KEYBOARD NINJA", 80, 80, self.WHITE)
            self.draw_text(self.screen, "WPM", 200, 40, self.MAIN_C)
            self.draw_text(self.screen, "Galaxy Shoot", 300, 40, self.MAIN_C)
            pygame.draw.rect(self.screen, self.MAIN_C, (75, 175, 650, 50), 2)
            pygame.draw.rect(self.screen, self.MAIN_C, (75, 275, 650, 50), 2)
            self.draw_text(self.screen, "Created by: ", 500, 40, self.MAIN_C)
            self.draw_text(self.screen, "Mauli Patel", 545, 40, self.MAIN_C)
            self.draw_text(self.screen, "Aditi Singh", 585, 40, self.MAIN_C)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if x >= 75 and x <= 650 and y >= 175 and y <= 225:
                        print("WPM")
                        WPM.WPM_call()
                    if x >= 75 and x <= 650 and y >= 275 and y <= 325:
                        print("Galaxy Shoot")
                        GalaxyShoot.GalaxyShoot_call()
                    print("Game over: back to main")



KeyboardNinja().run_game()

