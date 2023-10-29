import pygame
from player import Spaceship
from background_effects import Effects


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 900
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BACKGROUND = pygame.image.load("images/background.jpg")
CLOCK = pygame.time.Clock()


spaceship = Spaceship(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 300, WINDOW, WINDOW_WIDTH)
speed_effects = Effects(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW)


def game() -> None:
    speed_effects.update_effects()

    spaceship.moving(speed_effects.effects)
    spaceship.update()
    spaceship.fire_effect()

    pygame.display.update()
    CLOCK.tick(60)


def main_loop() -> None:
    helper = 0
    counter = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timer = pygame.time.get_ticks() / 1000
        WINDOW.blit(BACKGROUND, (-250, 0))

        if timer - helper >= 0.5:

            if counter % 2 == 0:
                speed_effects.speed_effect_1()
            else:
                speed_effects.speed_effect_2()

            helper = timer
            counter += 1

        game()


if __name__ == "__main__":
    main_loop()
