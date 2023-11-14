from typing import Tuple
from keyboard import is_pressed
from tkinter import TclError
import turtle


class Player:
    def __init__(self, size: tuple[int, int], color: str) -> None:
        self._player = turtle.Turtle()
        self._player.speed(0)
        self._player.shape("square")
        self._player.shapesize(*size)
        self._player.color(color)
        self._player.penup()
        self.size = size

    def set_position(self, position: Tuple[int, int]) -> None:
        self._player.setpos(*position)

    @property
    def vertical_position(self) -> float:
        return self._player.ycor()

    @vertical_position.setter
    def vertical_position(self, value: int) -> None:
        self._player.sety(value)


class Game:
    MOVEMENT_SPEED = 2

    def __init__(self, window: turtle.Screen, left_player: Player, right_player: Player) -> None:
        self._window = window
        self._left_player = left_player
        self._right_player = right_player
        self.running = True

    def players_movement(self) -> None:
        if not (is_pressed("w") and is_pressed("s")):
            if is_pressed("w"):
                self._left_player.vertical_position = self._left_player.vertical_position + self.MOVEMENT_SPEED
            elif is_pressed("s"):
                self._left_player.vertical_position = self._left_player.vertical_position - self.MOVEMENT_SPEED

        if not (is_pressed("Up") and is_pressed("Down")):
            if is_pressed("Up"):
                self._right_player.vertical_position = self._right_player.vertical_position + self.MOVEMENT_SPEED
            elif is_pressed("Down"):
                self._right_player.vertical_position = self._right_player.vertical_position - self.MOVEMENT_SPEED

    def block_arena_exit(self) -> None:
        if (self._left_player.vertical_position <=
                -self._window.window_height() // 2 + self._left_player.size[0] * 10 + 10):
            self._left_player.vertical_position = (
                    -self._window.window_height() // 2 + self._left_player.size[0] * 10 + 10)

        elif (self._left_player.vertical_position >=
                self._window.window_height() // 2 - self._left_player.size[0] * 10):
            self._left_player.vertical_position = (
                    self._window.window_height() // 2 - self._left_player.size[0] * 10)

        if (self._right_player.vertical_position <=
                -self._window.window_height() // 2 + self._right_player.size[0] * 10 + 10):
            self._right_player.vertical_position = (
                    -self._window.window_height() // 2 + self._right_player.size[0] * 10 + 10)

        elif (self._right_player.vertical_position >=
                self._window.window_height() // 2 - self._right_player.size[0] * 10):
            self._right_player.vertical_position = (
                    self._window.window_height() // 2 - self._right_player.size[0] * 10)

    def main_loop(self) -> None:
        while self.running:
            self.players_movement()
            self.block_arena_exit()
            self._window.update()


def main() -> None:
    WINDOW_WIDTH = 1800
    WINDOW_HEIGHT = 800

    window = turtle.Screen()
    window.title("PONG")
    window.bgcolor("black")
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.tracer(0)
    window.cv._rootwindow.resizable(False, False)

    PLAYERS_SIZE = (10, 1)
    PLAYERS_COLOR = "red"
    DISTANCE_FROM_WINDOW_EDGE = 20

    left_player = Player(PLAYERS_SIZE, PLAYERS_COLOR)
    right_player = Player(PLAYERS_SIZE, PLAYERS_COLOR)

    left_player.set_position((-WINDOW_WIDTH // 2 + DISTANCE_FROM_WINDOW_EDGE, 0))
    right_player.set_position((WINDOW_WIDTH // 2 - (DISTANCE_FROM_WINDOW_EDGE + 5), 0))

    try:
        game = Game(window, left_player, right_player)
        game.main_loop()
    except TclError:
        pass


if __name__ == "__main__":
    main()


# import turtle
# from winsound import Beep
# from random import randrange
# from time import sleep, time
#
# #WINDOW SIZE
# WIDTH = 1800
# HEIGHT = 800
#
# #CREATE THE WINDOW
# window = turtle.Screen()
# window.title('PONG')
# window.setup(WIDTH, HEIGHT)
# window.bgcolor('black')
# window.tracer(0)
#
# #QUIT THE PROGRAM
# def quit():
#     global running
#     running = False
#
# SIZE = 10
# #CREATE A PLAYER 1 (LEFT PLAYER)
# player_1 = turtle.Turtle()
# player_1.speed(0)
# player_1.shape('square')
# player_1.shapesize(SIZE, 1)
# player_1.color('red')
# player_1.penup()
# player_1.goto(-WIDTH/2 + 20, 0)
#
# #CREATE A PLAYER 2 (RIGHT PLAYER)
# player_2 = turtle.Turtle()
# player_2.speed(0)
# player_2.shape('square')
# player_2.shapesize(SIZE, 1)
# player_2.color('red')
# player_2.penup()
# player_2.goto(WIDTH/2 - 30, 0)
#
# #CREATE A BALL
# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape('square')
# ball.color('blue')
# ball.penup()
#
# #SPEED OF BALL AND PLAYERS
# ball.speed_x = ball.speed_y = 0.5
# speed_of_movement = 10
#
# #CREATE A PLAYERS MOVE
# def go_up_1():
#     player_1.sety(player_1.ycor() + speed_of_movement)
#
# def go_down_1():
#     player_1.sety(player_1.ycor() - speed_of_movement)
#
# def go_up_2():
#     player_2.sety(player_2.ycor() + speed_of_movement)
#
# def go_down_2():
#     player_2.sety(player_2.ycor() - speed_of_movement)
#
# #PLAYERS ACTIONS
# window.listen()
# window.onkeypress(quit, 'q') or window.onkeypress(quit, 'Q')
# window.onkeypress(go_up_1, 'w') or window.onkeypress(go_up_1, 'W')
# window.onkeypress(go_down_1, 's') or window.onkeypress(go_down_1, 'S')
# window.onkeypress(go_up_2, 'Up')
# window.onkeypress(go_down_2, 'Down')
#
# #DISPLAY PLAYER NAMES
# players = turtle.Turtle()
# players.speed(0)
# players.hideturtle()
# players.color('orange')
# players.penup()
# players.goto(-WIDTH / 2 + 40, HEIGHT / 2 - 40)
# players.write(f'PLAYER 1', font=('Arial', 20, 'normal'))
# players.goto(WIDTH / 2 - 180, HEIGHT / 2 - 40)
# players.write(f'PLAYER 2', font=('Arial', 20, 'normal'))
#
# #CREATE NOTIFICATION
# notification = turtle.Turtle()
# notification.speed(0)
# notification.hideturtle()
# notification.color('pink')
# notification.penup()
# notification.goto(-125, -HEIGHT / 2 + 50)
# notification.write('IF YOU WANT QUIT THE GAME PRESS Q', font=('Arial', 10, 'normal'))
#
# #DISPLAY GAME RESULTS
# score = turtle.Turtle()
# score.speed(0)
# score.hideturtle()
# score.color('purple')
# score.penup()
# score.goto(int((-WIDTH / 100) * 43), int(-HEIGHT / 20 - 10))
#
# #RANDOM START
# side_x, side_y = randrange(-1, 2, 2), randrange(-1, 2, 2)
#
# #CREATE GAME TIMER
# game_time = turtle.Turtle()
# game_time.speed(0)
# game_time.hideturtle()
# game_time.color('white')
# game_time.penup()
# game_time.goto(-75, HEIGHT / 2 - 50)
#
# start_time = previous_time = time()
#
# running = True
# while running:
#     window.update()
#
#     #TIMER
#     t = time()
#     elapsed_time = t - previous_time
#     if elapsed_time >= 1:
#         game_time.clear()
#         game_time.write(f'GAME TIME: {int(t - start_time)} s', font=('Arial', 15, 'normal'))
#         previous_time = t
#
#     #MOVMENT OF THE BALL
#     ball.setx(ball.xcor() + ball.speed_x * side_x)
#     ball.sety(ball.ycor() + ball.speed_y * side_y)
#
#     #BOUNCING OFF THE TOP AND BOTTOM WALLS OF THE BALL
#     if ball.ycor() >= HEIGHT / 2 - 10 or ball.ycor() <= -HEIGHT / 2 + 15:
#         ball.speed_y *= -1
#         Beep(1000, 5)
#
#     #BOUNCING THE BALL BY PLAYERS
#     if ball.xcor() == -WIDTH / 2 + 40 and player_1.ycor() + SIZE*10 >= ball.ycor() >= player_1.ycor() - SIZE*10 or \
#             ball.xcor() == WIDTH / 2 - 50 and player_2.ycor() + SIZE * 10 >= ball.ycor() >= player_2.ycor() - SIZE * 10:
#         ball.speed_x *= -1
#         Beep(1000, 5)
#
#     #BOUNCING THE BALL WITH THE TOP EDGE
#     if -WIDTH / 2 + 10 <= ball.xcor() <= -WIDTH / 2 + 39 \
#             and player_1.ycor() + SIZE*10 + 10 >= ball.ycor() >= player_1.ycor() + SIZE * 10 or \
#             WIDTH / 2 - 10 >= ball.xcor() >= WIDTH / 2 - 49 \
#             and player_2.ycor() + SIZE * 10 + 10 >= ball.ycor() >= player_2.ycor() + SIZE * 10:
#         ball.sety(ball.ycor() + 10)
#         ball.speed_y *= -1
#         Beep(1000, 5)
#
#     # BOUNCING THE BALL WITH THE BOTTOM EDGE
#     if -WIDTH / 2 + 10 <= ball.xcor() <= -WIDTH / 2 + 39 \
#             and player_1.ycor() - SIZE*10 - 10 <= ball.ycor() <= player_1.ycor() - SIZE * 10 or \
#             WIDTH / 2 - 10 >= ball.xcor() >= WIDTH / 2 - 49 \
#             and player_2.ycor() - SIZE * 10 - 10 <= ball.ycor() <= player_2.ycor() - SIZE * 10:
#         ball.sety(ball.ycor() - 10)
#         ball.speed_y *= -1
#         Beep(1000, 5)
#
#     #BLOCKING THE EXIT FROM THE ARENA (PLAYER 1)
#     if player_1.ycor() <= -HEIGHT / 2 + SIZE*10 + 10:
#         player_1.sety(-HEIGHT / 2 + SIZE*10 + 10)
#
#     if player_1.ycor() >= HEIGHT / 2 - SIZE*10:
#         player_1.sety(HEIGHT / 2 - SIZE*10)
#
#     #BLOCKING THE EXIT FROM THE ARENA (PLAYER 2)
#     if player_2.ycor() <= -HEIGHT / 2 + SIZE*10 + 10:
#         player_2.sety(-HEIGHT / 2 + SIZE*10 + 10)
#
#     if player_2.ycor() >= HEIGHT / 2 - SIZE*10:
#         player_2.sety(HEIGHT / 2 - SIZE*10)
#
#     #ENDING THE GAME
#     if ball.xcor() < -WIDTH / 2 + 5 or ball.xcor() > WIDTH / 2 - 5:
#         notification.clear()
#         Beep(500, 100)
#         #IF PLAYER 1 IS WINNER
#         if ball.xcor() > 0:
#             score.write(f'THE WINNER IS PLAYER 1', font=('Arial', int(WIDTH/20), 'normal')) #80
#         #IF PLAYER 2 IS WINNER
#         else:
#             score.write(f'THE WINNER IS PLAYER 2', font=('Arial', int(WIDTH/20), 'normal'))
#
#         #GAME CLOSURE NOTIFICATION
#         notification.goto(-300, -350)
#         for i in range(6):
#             countdown = (i - 5) * -1
#             if countdown == 1:
#                 notification.write(f'THE PROGRAM WILL CLOSE AFTER 1 SECOND', font=('Arial', 20, 'normal'))
#             elif countdown == 0:
#                 notification.goto(-42, -350)
#                 notification.write('BYE', font=('Arial', 30, 'normal'))
#             else:
#                 notification.write(f'THE PROGRAM WILL CLOSE AFTER {countdown} SECONDS', font=('Arial', 20, 'normal'))
#
#             sleep(1)
#             notification.clear()
#
#         running = False
