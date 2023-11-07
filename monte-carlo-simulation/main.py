import turtle
from typing import Tuple
from random import randint
from math import sqrt
from time import sleep
from tkinter import TclError


class Colors:
    BACKGROUND: str = "black"
    MAIN: str = "white"
    EFFECT: str = "blue"
    CORRECT: str = "green"
    INCORRECT: str = "red"


class MonteCarloBoard:
    def __init__(self, square_color: str, circle_color: str, board_length: int) -> None:
        self.square_color = square_color
        self.circle_color = circle_color
        self.board_length = board_length

    def square(self) -> None:
        turtle.color(self.square_color)
        for _ in range(4):
            turtle.forward(self.board_length)
            turtle.left(90)

    def circle(self) -> None:
        turtle.color(self.circle_color)
        turtle.circle(self.board_length // 2)

    def draw(self) -> None:
        self.square()
        turtle.pu()
        turtle.setx(turtle.pos()[0] + self.board_length // 2)
        turtle.pd()
        self.circle()


def draw_data(
        data: Tuple,
        font_size: int,
        font_name: str = "normal",
        font_type: str = "normal",
        turtle_to_draw: turtle.Turtle = turtle,
) -> None:
    start_y_position = turtle_to_draw.pos()[1]
    for index, data in enumerate(data):
        turtle_to_draw.sety(start_y_position - index * (font_size * 4))
        turtle_to_draw.write(data, font=(font_name, font_size, font_type))


def simulation(board_start_position: Tuple[float, float], board_length: int, font_size: int) -> None:
    DOT_SIZE = 2
    dots_in_circle = all_dots = 0
    half_of_board_length = board_length // 2

    turtle_to_changing_data = turtle.Turtle()
    turtle_to_changing_data.ht()
    turtle_to_changing_data.speed(0)
    turtle_to_changing_data.color(Colors.MAIN)
    turtle_to_changing_data.pu()
    turtle_to_changing_data.setx(board_start_position[0] - 200)

    while True:
        point_x_position = randint(0, board_length)
        point_y_position = randint(0, board_length)
        turtle.pu()
        turtle.goto(point_x_position + board_start_position[0], point_y_position + board_start_position[1])
        turtle.pd()

        all_dots += 1
        if ((
                sqrt(
                (point_x_position - half_of_board_length) ** 2 +
                (point_y_position - half_of_board_length) ** 2
                )) <= half_of_board_length):
            turtle.dot(DOT_SIZE, Colors.CORRECT)
            dots_in_circle += 1
        else:
            turtle.dot(DOT_SIZE, Colors.INCORRECT)

        number_pi = (dots_in_circle * 4) / all_dots

        turtle_to_changing_data.sety(board_start_position[1] + board_length - font_size * 3)

        data_to_draw = (number_pi, dots_in_circle, all_dots - dots_in_circle, all_dots)
        draw_data(data_to_draw, font_size, turtle_to_draw=turtle_to_changing_data)

        sleep(0.2)
        turtle_to_changing_data.clear()


def main() -> None:
    WIDTH = 500
    HEIGHT = 500

    window = turtle.Screen()
    window.setup(WIDTH, HEIGHT)
    window.bgcolor(Colors.BACKGROUND)
    window.title("Number pi by method - Monte Carlo")

    turtle.speed(0)
    turtle.ht()

    BOARD_LENGTH = 200
    FONT_SIZE = 15

    turtle.sety(-BOARD_LENGTH // 2)
    board_start_position = turtle.pos()

    board = MonteCarloBoard(Colors.EFFECT, Colors.MAIN, BOARD_LENGTH)
    board.draw()

    DATA_INFO_TO_DRAW = ("Number:", "Green points:", "Red points:", "All points:")
    turtle.color(Colors.EFFECT)
    turtle.pu()
    turtle.goto(board_start_position[0] - 200, board_start_position[1] + BOARD_LENGTH - FONT_SIZE)
    draw_data(DATA_INFO_TO_DRAW, FONT_SIZE)

    simulation(board_start_position, BOARD_LENGTH, FONT_SIZE)


if __name__ == "__main__":
    try:
        main()
    except (turtle.Terminator, TclError):
        pass
