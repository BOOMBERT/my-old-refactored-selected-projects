import pygame


class SpeedEffect:
    def __init__(self, x_pos_value: int, window: any):
        self.effect_x_pos = x_pos_value
        self.effect_y_pos = -200
        self.img = pygame.image.load("images/speed_line.png")
        self.window = window

    def update(self):
        self.window.blit(self.img, (self.effect_x_pos, self.effect_y_pos))
        self.effect_y_pos += 10


class Effects:
    def __init__(self, window_width: int, window_height: int, window: any):
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        self.effects = []

    def speed_effect_1(self):
        positions = [100, self.window_width // 2, self.window_width - 100]

        for position in positions:
            self.effects.append(SpeedEffect(position, self.window))

    def speed_effect_2(self):
        positions = [self.window_width // 2 - 100, self.window_width // 2 + 100]

        for position in positions:
            self.effects.append(SpeedEffect(position, self.window))

    def update_effects(self):
        for effect in self.effects:
            if effect.effect_y_pos > self.window_height + 300:
                self.effects.remove(effect)
            else:
                effect.update()
