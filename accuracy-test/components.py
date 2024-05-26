import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, horizontal_position: int, vertical_position: int, image: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (horizontal_position, vertical_position)

    def change_image(self, new_image: str) -> None:
        self.image = pygame.image.load(new_image)
        self.rect = self.image.get_rect(center=self.rect.center)

class Player(pygame.sprite.Sprite):
    def __init__(self, image: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(0, 0, 8, 8)

    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()
