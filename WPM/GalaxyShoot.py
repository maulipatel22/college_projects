import time
import pygame
import random


class GalaxyShoot_Game():
    def __init__(self):
        self.active = False
        self.end = False
        self.WHITE = [255, 255, 255]
        self.ORANGE = [255, 127, 0]
        self.SIZE = [800, 600]
        self.WIDTH = 800
        self.HEIGHT = 600
        self.BLACK = [0, 0, 0]
        self.input_text = ''
        self.done = False
        self.fruits_on_screen = []
        self.removed_fruits = []

        pygame.init()

        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Galaxy Shoot")
        self.clock = pygame.time.Clock()
        self.open_img = pygame.image.load('background.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.WIDTH, self.HEIGHT))


    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.WIDTH / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def show_results(self, screen):
        if (not self.end):
            if self.input_text in self.fruits_on_screen:
                self.removed_fruits = []
                self.fruits_on_screen.remove(self.input_text)
                self.removed_fruits.append(self.input_text)
                self.input_text = ''
            else:
                self.end_game()
                self.screen.fill((0, 0, 0), (0, 0, 800, 600))
                pygame.display.update()
                return True
            pygame.display.update()


    def run(self):
        self.reset_screen(self.fruits_on_screen)
        clock = pygame.time.Clock()

        while not self.done:
            self.screen.fill(self.BLACK)
            pygame.draw.rect(self.screen, self.ORANGE, (75, 500, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 525, 26, self.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    self.screen.fill((0, 0, 0), (0, 0, 800, 600))
                    pygame.display.update()
                    return True

                elif event.type == pygame.MOUSEBUTTONUP:
                    x_coor, y_coor = pygame.mouse.get_pos()
                    if x_coor >= 75 and x_coor <= 725 and y_coor >= 500 and y_coor <= 550:
                        self.active = True
                        self.input_text = ''
                if len(self.fruits_on_screen) == 0:
                    self.reset_screen(self.fruits_on_screen)

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            if self.show_results(self.screen):
                                return True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                                self.draw_text(self.screen, self.input_text, 525, 26, self.WHITE)

                            except:
                                pass

            pygame.display.update()

            for key in self.fruits.keys():
                if key == 'apple.jpg':
                    fruit = 'apple.jpg'
                if key == 'banana.png':
                    fruit = 'banana.png'
                if key == 'kiwi.png':
                    fruit = 'kiwi.png'
                if key == 'grapes.png':
                    fruit = 'grapes.png'
                if key == 'strawberry.jpg':
                    fruit = 'strawberry.jpg'
                if key == 'melon.jpg':
                    fruit = 'melon.jpg'
                if key == 'orange.jpg':
                    fruit = 'orange.jpg'
                if key[:-4] in self.removed_fruits:
                    continue
                fruit_img = pygame.image.load(fruit)
                fruit_img = pygame.transform.scale(fruit_img, (50, 50))

                self.fruits[key][1] += 2

                if self.fruits[key][1] > 550:
                    self.end_game()
                    self.screen.fill((0, 0, 0), (0, 0, 800, 600))
                    pygame.display.update()
                    return True

                self.screen.blit(fruit_img, (self.fruits[key][0], self.fruits[key][1]))
                pygame.display.update()
            pygame.display.flip()
            clock.tick(20)

    def reset_screen(self, fruit_on_screen):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)
        self.input_text = ''
        self.end = False
        self.fruits = {}

        fruit1_x = random.randrange(100, 400)
        fruit1_y = 0
        fruit2_x = random.randrange(450, 700)
        fruit2_y = 0
        random_fruit_1 = random.choice(
            ['apple.jpg', 'banana.png', 'kiwi.png', 'grapes.png', 'strawberry.jpg', 'melon.jpg', 'orange.jpg'])
        self.fruits[random_fruit_1] = [fruit1_x, fruit1_y]
        random_fruit_2 = random_fruit_1
        while random_fruit_2 == random_fruit_1:
            random_fruit_2 = random.choice(
            ['apple.jpg', 'banana.png', 'kiwi.png', 'grapes.png', 'strawberry.jpg', 'melon.jpg', 'orange.jpg'])
        self.fruits[random_fruit_1] = [fruit1_x, fruit1_y]
        self.fruits[random_fruit_2] = [fruit2_x, fruit2_y]
        self.fruits_on_screen.append(random_fruit_1[:-4])
        self.fruits_on_screen.append(random_fruit_2[:-4])

        """for i in range(2):
            x = random.randrange(100, 700)
            y = random.randrange(0, 50)
            random_fruit = random.choice(
                ['apple.jpg', 'banana.png', 'kiwi.png', 'grapes.png', 'strawberry.jpg', 'melon.jpg', 'orange.jpg'])
            self.fruits[random_fruit] = [x, y]
            self.fruits_on_screen.append(random_fruit[:-4])
            """
        print(self.fruits_on_screen)

    def end_game(self):

        self.screen.fill(self.WHITE, (0, 0, 800, 600))
        self.draw_text(self.screen, "GAME OVER", 50, 100, (0, 0, 0))
        time.sleep(3)



def GalaxyShoot_call():
    GalaxyShoot_Game().run()

