from typing import Tuple
from turtle import Turtle
from keyboard import is_pressed
from random import choice

from helper import to_px


class Player:
    def __init__(
            self,
            position: Tuple[int, int],
            size: Tuple[int, int],
            color: str,
            keys_to_move: Tuple[str, str],
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
        self.keys_to_move = keys_to_move
        self.movement_speed = movement_speed

    def get_horizontal_position(self) -> float:
        return self._player.xcor()

    def get_vertical_position(self) -> float:
        return self._player.ycor()

    def movement(self) -> None:
        if not (is_pressed(self.keys_to_move[0]) and is_pressed(self.keys_to_move[1])):
            if is_pressed(self.keys_to_move[0]):
                self._player.sety(self._player.ycor() + self.movement_speed)
            elif is_pressed(self.keys_to_move[1]):
                self._player.sety(self._player.ycor() - self.movement_speed)

    def block_area_exit(self, window_height: int) -> None:
        half_of_player_height_in_px = to_px(self.size[0]) / 2
        if self._player.ycor() <= -window_height / 2 + half_of_player_height_in_px:
            self._player.sety(-window_height / 2 + half_of_player_height_in_px)

        elif self._player.ycor() >= window_height / 2 - half_of_player_height_in_px:
            self._player.sety(window_height / 2 - half_of_player_height_in_px)


class Ball:
    def __init__(self, size: int, color: str, ball_speed: float) -> None:
        self._ball = Turtle()
        self._ball.speed(0)
        self._ball.shape("square")
        self._ball.shapesize(size)
        self._ball.color(color)
        self._ball.penup()
        self.size = size
        self.speed = ball_speed
        self.horizontal_trajectory = choice([-1, 1])
        self.vertical_trajectory = choice([-1, 1])

    def get_horizontal_position(self) -> float:
        return self._ball.xcor()

    def get_vertical_position(self) -> float:
        return self._ball.ycor()

    def movement(self) -> None:
        self._ball.setx(self._ball.xcor() + self.speed * self.horizontal_trajectory)
        self._ball.sety(self._ball.ycor() + self.speed * self.vertical_trajectory)

    def block_area_exit(self, window_height: int) -> None:
        half_of_ball_size_in_px = to_px(self.size) / 2
        if (
                self._ball.ycor() <= -window_height / 2 + half_of_ball_size_in_px or
                self._ball.ycor() >= window_height / 2 - half_of_ball_size_in_px
        ):
            self.vertical_trajectory *= -1
