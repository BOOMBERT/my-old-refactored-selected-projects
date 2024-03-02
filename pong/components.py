from typing import Tuple
from turtle import Turtle
from keyboard import is_pressed
from random import choice
from time import sleep

from helper import to_px, turtle_setup


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
        self._ball = turtle_setup(color)
        self._ball.shape("square")
        self._ball.shapesize(size)
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


class DisplayInfo:
    def __init__(self, window_width: int, window_height: int, font_size: int) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.font_size = font_size
        self.font = ("Arial", font_size, "normal")
        self.timer_turtle = turtle_setup("purple")
        self.timer_turtle.ht()
        self.static_info_turtle = turtle_setup("purple")
        self.static_info_turtle.ht()

    def winner(self, name: str) -> None:
        winner_message = f"THE WINNER IS {name.upper()}"
        self.static_info_turtle.clear()
        self.static_info_turtle.goto(0, -self.window_height / 2 + self.font_size * 2)
        self.static_info_turtle.write(winner_message, align="center", font=self.font)

    def countdown_to_close_the_game(self) -> None:
        close_game_message = "THE GAME IS GOING TO CLOSE AFTER ? SECONDS"
        countdown_turtle = turtle_setup("blue")
        countdown_turtle.ht()
        countdown_turtle.goto(0, -self.font_size / 2)

        for countdown in range(5, -1, -1):
            close_game_message_with_countdown = close_game_message.replace("?", str(countdown))
            countdown_turtle.write(
                f"{close_game_message_with_countdown if countdown > 1 else close_game_message_with_countdown[:-1]}",
                align="center", font=self.font
            )

            sleep(1)
            if countdown == 0:
                countdown_turtle.clear()
                countdown_turtle.write("BYE :D", align="center", font=self.font)
                sleep(1)
            countdown_turtle.clear()

    def timer(self, time_in_seconds: int) -> None:
        timer_message = f"Elapsed time: {time_in_seconds}s"
        self.timer_turtle.clear()
        self.timer_turtle.goto(0, self.window_height / 2 - self.font_size * 2)
        self.timer_turtle.write(timer_message, align="center", font=self.font)

    def quit_the_game_option(self, key: str) -> None:
        quit_the_game_message = f"TO QUIT THE GAME PRESS {key.upper()}"
        self.static_info_turtle.goto(0, -self.window_height / 2 + self.font_size / 2)
        self.static_info_turtle.write(
            quit_the_game_message, align="center",
            font=(self.font[0], self.font[1] // 3, self.font[2])
        )
