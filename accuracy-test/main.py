import pygame
from typing import Literal, Tuple

from components import Button, Player, Target
from helper import get_initial_menu_button_schemas, get_target_image_by_difficulty_level, get_final_menu_button_schemas


BLACK_COLOR = (0, 0, 0)

class Game:
    def __init__(
            self,
            fps: int,
            title: str,
            window_size: Tuple[int, int],
            background_image: str,
            player_image: str,
            game_time: float
    ) -> None:
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(title)
        self.fps = fps
        self.window = pygame.display.set_mode(window_size)
        self.background = pygame.image.load(background_image)
        self.clock = pygame.time.Clock()
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.game_time = game_time
        self.player = Player(player_image)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.FONT = pygame.font.SysFont("Mono", 28)

    def initial_menu(self) -> Literal["easy", "normal", "hard"] | bool:
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

                    if pygame.sprite.spritecollide(self.player, play_button, False):
                        if easy_choiced:
                            return "easy"
                        elif normal_choiced:
                            return "normal"
                        elif hard_choiced:
                            return "hard"

            self.window.blit(self.background, (0, 0))

            play_button.draw(self.window)
            easy_button.draw(self.window)
            normal_button.draw(self.window)
            hard_button.draw(self.window)

            self.player_group.draw(self.window)
            self.player_group.update()

            pygame.display.flip()
            self.clock.tick(self.fps)

        return False

    def play(self, difficulty_level: Literal["easy", "normal", "hard"]) -> int | bool:
        target_image = get_target_image_by_difficulty_level(difficulty_level)
        target_group = pygame.sprite.Group()
        target_group.add(Target(self.window_width, self.window_height, target_image))

        score = 0
        start_time = pygame.time.get_ticks()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.sprite.spritecollide(self.player, target_group, True):
                        target_group.add(Target(self.window_width, self.window_height, target_image))
                        score += 1
                    else:
                        score -= 1

            remaining_game_time = self.game_time - (pygame.time.get_ticks() - start_time) / 1000
            if remaining_game_time <= 0:
                return score

            game_time_surface = self.FONT.render(f"Game time = {str(round(remaining_game_time, 1))}", True, BLACK_COLOR)
            score_surface = self.FONT.render(f"Current score = {str(score)}", True, BLACK_COLOR)

            self.window.blit(self.background, (0, 0))
            self.window.blit(
                game_time_surface,
                (game_time_surface.get_rect(center=self.window.get_rect().center)[0], 0)
            )
            self.window.blit(
                score_surface,
                (score_surface.get_rect(center=self.window.get_rect().center)[0], self.window_height - 75)
            )

            target_group.draw(self.window)

            self.player_group.draw(self.window)
            self.player_group.update()

            pygame.display.flip()
            self.clock.tick(self.fps)

        return False

    def final_menu(self, score: int) -> bool:
        buttons = get_final_menu_button_schemas(self.window_width, self.window_height)
        back_to_menu_button = pygame.sprite.Group()
        back_to_menu_button.add(Button(
            buttons["back_to_menu"]["horizontal_position"],
            buttons["back_to_menu"]["vertical_position"],
            buttons["back_to_menu"]["image"]
        ))

        exit_button = pygame.sprite.Group()
        exit_button.add(Button(
            buttons["exit"]["horizontal_position"],
            buttons["exit"]["vertical_position"],
            buttons["exit"]["image"]
        ))

        back_to_menu_button_hovered = exit_button_hovered = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if pygame.sprite.spritecollide(self.player, back_to_menu_button, False):
                    back_to_menu_button.sprites()[0].change_image(buttons["back_to_menu"]["hovered_image"])
                    back_to_menu_button_hovered = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return True
                else:
                    if back_to_menu_button_hovered:
                        back_to_menu_button.sprites()[0].change_image(buttons["back_to_menu"]["image"])
                        back_to_menu_button_hovered = False

                if pygame.sprite.spritecollide(self.player, exit_button, False):
                    exit_button.sprites()[0].change_image(buttons["exit"]["hovered_image"])
                    exit_button_hovered = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return False
                else:
                    if exit_button_hovered:
                        exit_button.sprites()[0].change_image(buttons["exit"]["image"])
                        exit_button_hovered = False

            score_surface = self.FONT.render(f"Your score = {str(score)}", True, BLACK_COLOR)

            self.window.blit(self.background, (0, 0))
            self.window.blit(
                score_surface,
                (score_surface.get_rect(center=self.window.get_rect().center)[0], self.window_height - 75)
            )

            back_to_menu_button.draw(self.window)
            exit_button.draw(self.window)

            self.player_group.draw(self.window)
            self.player_group.update()

            pygame.display.flip()
            self.clock.tick(self.fps)

        return False


def main():
    FPS = 60
    GAME_TITLE = "ACCURACY TESTER"
    WINDOW_WIDTH, WINDOW_HEIGHT = 1270, 720
    BACKGROUND_IMAGE_PATH = "assets/game/background_image.jpg"
    PLAYER_IMAGE_PATH = "assets/game/crosshair.png"
    GAME_TIME = 10 # Game time is given in seconds.

    game = Game(FPS, GAME_TITLE, (WINDOW_WIDTH, WINDOW_HEIGHT), BACKGROUND_IMAGE_PATH, PLAYER_IMAGE_PATH, GAME_TIME)
    while True:
        if (difficulty_level := game.initial_menu()) is False:
            break
        if (final_score := game.play(difficulty_level)) is False:
            break
        if game.final_menu(final_score) is False:
            break


if __name__ == '__main__':
    main()
