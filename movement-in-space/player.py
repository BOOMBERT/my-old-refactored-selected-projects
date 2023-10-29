import pygame


class Spaceship:
    def __init__(self, x_pos: int, y_pos: int, window: any, window_width: int) -> None:
        self.player_x_pos = x_pos
        self.player_y_pos = y_pos
        self.window = window
        self.window_width = window_width
        self.img = pygame.image.load("images/player.png")

        self.any_move = False

        self.fire_img = "images/fire_effect/flame_"
        self.animations = 4 * [None]
        self.step_index = 0

    def moving(self, effects: list[any]) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.player_x_pos < self.window_width - 100:
            self.any_move = True
            self.img = pygame.image.load("images/player_right.png")
            self.player_x_pos += 5
            for effect in effects:
                effect.effect_x_pos -= 2

        if keys[pygame.K_LEFT] and self.player_x_pos > 0:
            self.any_move = True
            self.img = pygame.image.load("images/player_left.png")
            self.player_x_pos -= 5
            for effect in effects:
                effect.effect_x_pos += 2

        if not any(keys) and self.any_move:
            self.any_move = False
            self.img = pygame.image.load("images/player.png")

    def fire_effect(self) -> None:
        self.animations[self.step_index] = pygame.image.load(
            self.fire_img + str(self.step_index) + ".png")

        if self.any_move:
            fire_x_position = self.player_x_pos + 35
        else:
            fire_x_position = self.player_x_pos + 40

        self.window.blit(self.animations[self.step_index],
                         (fire_x_position, self.player_y_pos + 75))
        self.step_index += 1

        if self.step_index >= len(self.animations):
            self.step_index = 0

    def update(self) -> None:
        self.window.blit(self.img, (self.player_x_pos, self.player_y_pos))
