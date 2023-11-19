from typing import Tuple
from turtle import Turtle
from keyboard import is_pressed
from random import choice


class Player:
    def __init__(
            self,
            position: Tuple[int, int],
            size: Tuple[int, int],
            color: str,
            moving_keys: Tuple[str, str],
            movement_speed: int
    ) -> None:
        self._player = Turtle()
        self._player.speed(0)
        self._player.shape("square")
        self._player.shapesize(*size)
        self._player.color(color)
        self._player.penup()
        self._player.setposition(*position)
        self.size = size
        self.moving_keys = moving_keys
        self.movement_speed = movement_speed

    def movement(self) -> None:
        if not (is_pressed(self.moving_keys[0]) and is_pressed(self.moving_keys[1])):
            if is_pressed(self.moving_keys[0]):
                self._player.sety(self._player.ycor() + self.movement_speed)
            elif is_pressed(self.moving_keys[1]):
                self._player.sety(self._player.ycor() - self.movement_speed)

    def block_area_exit(self, window_height: int) -> None:
        if self._player.ycor() <= -window_height // 2 + self.size[0] * 10 + 10:
            self._player.sety(-window_height // 2 + self.size[0] * 10 + 10)

        elif self._player.ycor() >= window_height // 2 - self.size[0] * 10:
            self._player.sety(window_height // 2 - self.size[0] * 10)


class Ball:
    def __init__(self, size: int, color: str, ball_speed: float) -> None:
        self._ball = Turtle()
        self._ball.speed(0)
        self._ball.shape("square")
        self._ball.shapesize(size)
        self._ball.color(color)
        self._ball.penup()
        self.ball_speed = ball_speed
        self.horizontal_trajectory = choice([-1, 1])
        self.vertical_trajectory = choice([-1, 1])

    def movement(self) -> None:
        self._ball.setx(self._ball.xcor() + self.ball_speed * self.horizontal_trajectory)
        self._ball.sety(self._ball.ycor() + self.ball_speed * self.vertical_trajectory)
