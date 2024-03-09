from tkinter import TclError
from turtle import Screen, mainloop, Terminator
from keyboard import is_pressed
from time import time

from components import Player, Ball, DisplayInfo
from helper import to_px


class Game:
    def __init__(
            self,
            window: Screen,
            left_player: Player,
            right_player: Player,
            ball: Ball,
            font_size: int,
            quit_the_game_key: str = "q"
    ) -> None:
        self._window = window
        self._left_player = left_player
        self._right_player = right_player
        self._ball = ball
        self.window_width = window.window_width()
        self.window_height = window.window_height()
        self.running = True
        self.delay = 1000 // 60
        self.ball_size_in_px = to_px(ball.size)
        self.quit_the_game_key = quit_the_game_key
        self.displaying = DisplayInfo(self.window_width, self.window_height, font_size)
        self.displaying.quit_the_game_option(quit_the_game_key)
        self.game_time = time()
        self.time_from_start_in_seconds = 0

    def players_control(self) -> None:
        self._left_player.movement()
        self._right_player.movement()

        self._left_player.block_area_exit(self.window_height)
        self._right_player.block_area_exit(self.window_height)

    def ball_control(self) -> None:
        self._ball.movement()
        self._ball.block_area_exit(self.window_height)

    def bounce_of_ball_of_top_edge_of_player(
            self,
            player_top_bounce_position: float,
            player_movement_speed: float
    ) -> bool:
        return (
                player_top_bounce_position - self._ball.speed - player_movement_speed <=
                self._ball.get_vertical_position()
                <= player_top_bounce_position
        )

    def bounce_of_ball_of_bottom_edge_of_player(
            self,
            player_bottom_bounce_position: float,
            player_movement_speed: float
    ) -> bool:
        return (
                player_bottom_bounce_position + self._ball.speed + player_movement_speed >=
                self._ball.get_vertical_position()
                >= player_bottom_bounce_position
        )

    def bounce_the_ball_by_right_player(
            self,
            player_width_in_px,
            player_height_in_px,
            player_bounce_horizontal_position
    ) -> None:
        player_top_bounce_position = (
                self._right_player.get_vertical_position() + player_height_in_px / 2 + self.ball_size_in_px / 2
        )
        player_bottom_bounce_position = (
                self._right_player.get_vertical_position() - player_height_in_px / 2 - self.ball_size_in_px / 2
        )

        if (
                player_bounce_horizontal_position <=
                self._ball.get_horizontal_position()
                < player_bounce_horizontal_position + self._ball.speed
                and
                player_top_bounce_position >
                self._ball.get_vertical_position()
                > player_bottom_bounce_position
        ):
            self._ball.horizontal_trajectory = -1

        if (
                player_bounce_horizontal_position <=
                self._ball.get_horizontal_position()
                <= player_bounce_horizontal_position +
                player_width_in_px + self.ball_size_in_px + self._ball.speed
        ):
            if self.bounce_of_ball_of_top_edge_of_player(
                    player_top_bounce_position, self._right_player.movement_speed
            ):
                self._ball.vertical_trajectory = 1

            elif self.bounce_of_ball_of_bottom_edge_of_player(
                    player_bottom_bounce_position, self._right_player.movement_speed
            ):
                self._ball.vertical_trajectory = -1

    def bounce_the_ball_by_left_player(
            self,
            player_width_in_px,
            player_height_in_px,
            player_bounce_horizontal_position
    ) -> None:
        player_top_bounce_position = (
                self._left_player.get_vertical_position() + player_height_in_px / 2 + self.ball_size_in_px / 2
        )
        player_bottom_bounce_position = (
                self._left_player.get_vertical_position() - player_height_in_px / 2 - self.ball_size_in_px / 2
        )

        if (
                player_bounce_horizontal_position >=
                self._ball.get_horizontal_position()
                > player_bounce_horizontal_position - self._ball.speed
                and
                player_top_bounce_position >
                self._ball.get_vertical_position()
                > player_bottom_bounce_position
        ):
            self._ball.horizontal_trajectory = 1

        if (
                player_bounce_horizontal_position >=
                self._ball.get_horizontal_position()
                >= player_bounce_horizontal_position -
                player_width_in_px - self.ball_size_in_px - self._ball.speed
        ):
            if self.bounce_of_ball_of_top_edge_of_player(
                    player_top_bounce_position, self._left_player.movement_speed
            ):
                self._ball.vertical_trajectory = 1

            elif self.bounce_of_ball_of_bottom_edge_of_player(
                    player_bottom_bounce_position, self._left_player.movement_speed
            ):
                self._ball.vertical_trajectory = -1

    def bounce_the_ball_by_players(self) -> None:
        if self._ball.get_horizontal_position() > 0:
            if self._ball.horizontal_trajectory == 1:

                right_player_width_in_px = to_px(self._right_player.size[1])
                right_player_height_in_px = to_px(self._right_player.size[0])

                right_player_bounce_horizontal_position = (
                        self.window_width / 2 -
                        (self.window_width / 2 - self._right_player.get_horizontal_position()) -
                        right_player_width_in_px / 2 - self.ball_size_in_px / 2
                )

                self.bounce_the_ball_by_right_player(
                    right_player_width_in_px,
                    right_player_height_in_px,
                    right_player_bounce_horizontal_position
                )

        else:
            if self._ball.horizontal_trajectory == -1:

                left_player_width_in_px = to_px(self._left_player.size[1])
                left_player_height_in_px = to_px(self._left_player.size[0])

                left_player_bounce_horizontal_position = (
                        -self.window_width / 2 +
                        (self.window_width / 2 + self._left_player.get_horizontal_position()) +
                        left_player_width_in_px / 2 + self.ball_size_in_px / 2
                )

                self.bounce_the_ball_by_left_player(
                    left_player_width_in_px,
                    left_player_height_in_px,
                    left_player_bounce_horizontal_position
                )

    def quit_the_game_by_pressing_the_key(self) -> None:
        if is_pressed(self.quit_the_game_key):
            self.running = False

    def end_of_the_game(self) -> None:
        left_border = -self.window_width / 2 - self.ball_size_in_px / 2
        if self._ball.get_horizontal_position() < left_border:
            self.displaying.winner("RIGHT PLAYER")
            self.displaying.countdown_to_close_the_game()
            self.running = False
        elif self._ball.get_horizontal_position() > -left_border:
            self.displaying.winner("LEFT PLAYER")
            self.displaying.countdown_to_close_the_game()
            self.running = False

    def timer(self) -> None:
        time_now = time()
        elapsed_time = time_now - self.game_time
        if elapsed_time >= 1:
            self.time_from_start_in_seconds += 1
            self.game_time = time_now
            self.displaying.timer(self.time_from_start_in_seconds)

    def update_game(self) -> None:
        if self.running:
            self.timer()
            self.players_control()
            self.ball_control()
            self.bounce_the_ball_by_players()

            self.quit_the_game_by_pressing_the_key()
            self.end_of_the_game()

            self._window.update()
            self._window.ontimer(self.update_game, self.delay)

        else:
            self._window.bye()

    def main_loop(self) -> None:
        self.update_game()
        mainloop()


def main() -> None:
    WINDOW_WIDTH = 1800
    WINDOW_HEIGHT = 800

    window = Screen()
    window.title("PONG")
    window.bgcolor("black")
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.tracer(0)
    window.cv._rootwindow.resizable(False, False)

    PLAYERS_SIZE = (10, 1)
    PLAYERS_COLOR = "red"
    PLAYERS_MOVEMENT_SPEED = 10
    PLAYERS_DISTANCE_FROM_WINDOW_EDGE = 20

    left_player = Player(
        (-WINDOW_WIDTH // 2 + PLAYERS_DISTANCE_FROM_WINDOW_EDGE, 0),
        PLAYERS_SIZE,
        PLAYERS_COLOR,
        ("w", "s"),
        PLAYERS_MOVEMENT_SPEED
    )
    right_player = Player(
        (WINDOW_WIDTH // 2 - (PLAYERS_DISTANCE_FROM_WINDOW_EDGE + 7), 0),
        PLAYERS_SIZE,
        PLAYERS_COLOR,
        ("Up", "Down"),
        PLAYERS_MOVEMENT_SPEED
    )

    ball = Ball(4, "blue", 8)
    FONT_SIZE = 36

    try:
        game = Game(window, left_player, right_player, ball, FONT_SIZE)
        game.main_loop()
    except (TclError, Terminator):
        pass


if __name__ == "__main__":
    main()
