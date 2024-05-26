import pygame
from typing import Literal, Tuple

from components import Button, Player
from helper import get_initial_menu_button_schemas


class Game:
    def __init__(self, title: str, window_size: Tuple[int, int], background_image: str, player_image: str) -> None:
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(title)
        self.window = pygame.display.set_mode(window_size)
        self.background = pygame.image.load(background_image)
        self.clock = pygame.time.Clock()
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.player = Player(player_image)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

    def initial_menu(self) -> None:
        buttons = get_initial_menu_button_schemas(self.window_width, self.window_height)
        play_button = pygame.sprite.Group()
        play_button.add(Button(
            buttons["play"]["horizontal_position"], buttons["play"]["vertical_position"], buttons["play"]["image"]
        ))

        easy_button = pygame.sprite.Group()
        easy_button.add(Button(
            buttons["easy"]["horizontal_position"], buttons["easy"]["vertical_position"], buttons["easy"]["image"]
        ))

        normal_button = pygame.sprite.Group()
        normal_button.add(Button(
            buttons["normal"]["horizontal_position"], buttons["normal"]["vertical_position"], buttons["normal"]["image"]
        ))

        hard_button = pygame.sprite.Group()
        hard_button.add(Button(
            buttons["hard"]["horizontal_position"], buttons["hard"]["vertical_position"], buttons["hard"]["image"]
        ))

        easy_choiced = normal_choiced = hard_choiced = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.sprite.spritecollide(self.player, easy_button, False):
                        easy_button.sprites()[0].change_image(buttons["easy"]["choiced_image"])
                        easy_choiced = True

                        if normal_choiced:
                            normal_button.sprites()[0].change_image(buttons["normal"]["image"])
                            normal_choiced = False
                        elif hard_choiced:
                            hard_button.sprites()[0].change_image(buttons["hard"]["image"])
                            hard_choiced = False

                    if pygame.sprite.spritecollide(self.player, normal_button, False):
                        normal_button.sprites()[0].change_image(buttons["normal"]["choiced_image"])
                        normal_choiced = True

                        if easy_choiced:
                            easy_button.sprites()[0].change_image(buttons["easy"]["image"])
                            easy_choiced = False
                        elif hard_choiced:
                            hard_button.sprites()[0].change_image(buttons["hard"]["image"])
                            hard_choiced = False

                    if pygame.sprite.spritecollide(self.player, hard_button, False):
                        hard_button.sprites()[0].change_image(buttons["hard"]["choiced_image"])
                        hard_choiced = True

                        if easy_choiced:
                            easy_button.sprites()[0].change_image(buttons["easy"]["image"])
                            easy_choiced = False
                        elif normal_choiced:
                            normal_button.sprites()[0].change_image(buttons["normal"]["image"])
                            normal_choiced = False

            self.window.blit(self.background, (0, 0))

            play_button.draw(self.window)
            easy_button.draw(self.window)
            normal_button.draw(self.window)
            hard_button.draw(self.window)

            self.player_group.draw(self.window)
            self.player_group.update()

            pygame.display.flip()
            self.clock.tick(60)

    def start(self, difficulty_level: Literal["easy", "normal", "hard"]):
        pass

    def end_menu(self):
        pass


def main():
    GAME_TITLE = "Accuracy tester"
    WINDOW_WIDTH, WINDOW_HEIGHT = 1270, 720
    BACKGROUND_IMAGE_PATH = "assets/game/background_image.jpg"
    PLAYER_IMAGE_PATH = "assets/game/crosshair.png"

    game = Game(GAME_TITLE, (WINDOW_WIDTH, WINDOW_HEIGHT), BACKGROUND_IMAGE_PATH, PLAYER_IMAGE_PATH)
    game.initial_menu()

if __name__ == '__main__':
    main()


# import sys
# import random
# import pygame
#
# #CLASSES================================================================================================================
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("assets/game/crosshair.png")
#         self.rect = pygame.Rect(0, 0, 8, 8)
#
#     def update(self):
#         self.rect.center = pygame.mouse.get_pos()
#
#
# class Target(pygame.sprite.Sprite):
#     def __init__(self, target_img):
#         super().__init__()
#         self.image = pygame.image.load(target_img)
#         self.rect = self.image.get_rect()
#         self.x_cord = random.randint(self.rect[2] / 2, SCREEN_WIDTH - self.rect[2] / 2)
#         self.y_cord = random.randint(self.rect[3] / 2, SCREEN_HEIGHT - self.rect[3] / 2)
#         self.rect.center = (self.x_cord, self.y_cord)
#
#
# class Button(pygame.sprite.Sprite):
#     def __init__(self, x_cord, y_cord, button_image):
#         super().__init__()
#         self.image = pygame.image.load(button_image)
#         self.rect = self.image.get_rect()
#         self.x_cord = x_cord
#         self.y_cord = y_cord
#         self.rect.center = (self.x_cord, self.y_cord)
#
# #GAME_OPTIONS===========================================================================================================
# def exit_the_game():
#     pygame.quit()
#     sys.exit()
#
# pygame.init()
# pygame.display.set_caption('Accuracy tester')
# clock = pygame.time.Clock()
# SCREEN_WIDTH, SCREEN_HEIGHT = 1270, 720
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background = pygame.image.load("assets/game/background_image.jpg")
# pygame.mouse.set_visible(False)
#
# player = Player()
# player_group = pygame.sprite.Group()
# player_group.add(player)
#
# #GAME_MENU==============================================================================================================
# def main_menu():
#     play_button = pygame.sprite.Group()
#     play_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "assets/initial_menu/buttons/play.png"))
#
#     hard_button = pygame.sprite.Group()
#     hard_button.add(Button(200, 250, "assets/initial_menu/buttons/hard/base.png"))
#
#     normal_button = pygame.sprite.Group()
#     normal_button.add(Button(200, 350, "assets/initial_menu/buttons/normal/base.png"))
#
#     easy_button = pygame.sprite.Group()
#     easy_button.add(Button(200, 450, "assets/initial_menu/buttons/easy/base.png"))
#
#     hard_choiced = normal_choiced = easy_choiced = False
#
#     def hard_is_choiced():
#         hard_button.empty()
#         hard_button.add(Button(200, 250, "assets/initial_menu/buttons/hard/base.png"))
#
#     def normal_is_choiced():
#         normal_button.empty()
#         normal_button.add(Button(200, 350, "assets/initial_menu/buttons/normal/base.png"))
#
#     def easy_is_choiced():
#         easy_button.empty()
#         easy_button.add(Button(200, 450, "assets/initial_menu/buttons/easy/base.png"))
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit_the_game()
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if pygame.sprite.spritecollide(player, hard_button, True):
#                     if normal_choiced:
#                         normal_is_choiced()
#                         normal_choiced = False
#
#                     elif easy_choiced:
#                         easy_is_choiced()
#                         easy_choiced = False
#
#                     hard_button.add(Button(200, 250, "assets/initial_menu/buttons/hard/choice.png"))
#                     hard_choiced = True
#
#                 if pygame.sprite.spritecollide(player, normal_button, True):
#                     if hard_choiced:
#                         hard_is_choiced()
#                         hard_choiced = False
#
#                     elif easy_choiced:
#                         easy_is_choiced()
#                         easy_choiced = False
#
#                     normal_button.add(Button(200, 350, "assets/initial_menu/buttons/normal/choice.png"))
#                     normal_choiced = True
#
#                 if pygame.sprite.spritecollide(player, easy_button, True):
#                     if hard_choiced:
#                         hard_is_choiced()
#                         hard_choiced = False
#
#                     elif normal_choiced:
#                         normal_is_choiced()
#                         normal_choiced = False
#
#                     easy_button.add(Button(200, 450, "assets/initial_menu/buttons/easy/choice.png"))
#                     easy_choiced = True
#
#                 if pygame.sprite.spritecollide(player, play_button, True):
#                     if hard_choiced:
#                         game('hard')
#                     elif normal_choiced:
#                         game('normal')
#                     elif easy_choiced:
#                         game('easy')
#                     else:
#                         play_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "assets/game/play.png"))
#
#         screen.blit(background, (0, 0))
#
#         play_button.draw(screen)
#         hard_button.draw(screen)
#         normal_button.draw(screen)
#         easy_button.draw(screen)
#
#         player_group.draw(screen)
#         player_group.update()
#
#         pygame.display.flip()
#         clock.tick(144)
#
# #GAME===================================================================================================================
# def game(difficulty_level):
#     target_group = pygame.sprite.Group()
#
#     if difficulty_level == "hard":
#         img_target = "assets/game/target/hard_level.png"
#     elif difficulty_level == "normal":
#         img_target = "assets/game/target/normal_level.png"
#     else:
#         img_target = "assets/game/target/easy_level.png"
#
#     target_group.add(Target(img_target))
#
#     your_score = 0
#     start_time = pygame.time.get_ticks()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit_the_game()
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if pygame.sprite.spritecollide(player, target_group, True):
#                     target_group.add(Target(img_target))
#                     your_score += 1
#                 else:
#                     your_score -= 1
#
#         game_time = (pygame.time.get_ticks() - start_time) / 1000
#         if game_time >= 20:
#             end_menu(your_score)
#
#         screen.blit(background, (0, 0))
#
#         target_group.draw(screen)
#
#         player_group.draw(screen)
#         player_group.update()
#
#         pygame.display.flip()
#         clock.tick(144)
#
# #MENU_AFTER_GAME========================================================================================================
# def end_menu(score):
#     back_to_menu_button = pygame.sprite.Group()
#     back_to_menu_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "assets/final_menu/buttons/back_to_menu/base.png"))
#
#     exit_button = pygame.sprite.Group()
#     exit_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, "assets/final_menu/buttons/exit/base.png"))
#
#     font = pygame.font.Font(None, 50)
#     score_text = font.render(f'Your score {score}', False, (0, 0, 0))
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit_the_game()
#
#             if pygame.sprite.spritecollide(player, back_to_menu_button, True):
#                 back_to_menu_button.empty()
#                 back_to_menu_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "assets/final_menu/buttons/back_to_menu/hovered.png"))
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     main_menu()
#
#             else:
#                 back_to_menu_button.empty()
#                 back_to_menu_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "assets/final_menu/buttons/back_to_menu/base.png"))
#
#             if pygame.sprite.spritecollide(player, exit_button, True):
#                 exit_button.empty()
#                 exit_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, "assets/final_menu/buttons/exit/hovered.png"))
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     exit_the_game()
#
#             else:
#                 exit_button.empty()
#                 exit_button.add(Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, "assets/final_menu/buttons/exit/base.png"))
#
#         screen.blit(background, (0, 0))
#         screen.blit(score_text, ((SCREEN_WIDTH / 2) - (score_text.get_width() / 2), SCREEN_HEIGHT / 2 - 200))
#
#         back_to_menu_button.draw(screen)
#         exit_button.draw(screen)
#
#         player_group.draw(screen)
#         player_group.update()
#
#         pygame.display.flip()
#         clock.tick(144)
#
# #START==================================================================================================================
# if __name__ == '__main__':
#     main_menu()
