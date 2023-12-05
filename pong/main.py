from tkinter import TclError
from turtle import Screen, mainloop, Terminator

from components import Player, Ball
from helper import to_px


class Game:
    def __init__(self, window: Screen, left_player: Player, right_player: Player, ball: Ball) -> None:
        self._window = window
        self._left_player = left_player
        self._right_player = right_player
        self._ball = ball
        self.window_height = window.window_height()
        self.window_width = window.window_width()
        self.running = True
        self.delay = 1000 // 60
        self.ball_size_in_px = to_px(ball.size)

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

    def update_game(self) -> None:
        if self.running:
            self.players_control()
            self.ball_control()
            self.bounce_the_ball_by_players()

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

    ball = Ball(1, "blue", 5)

    try:
        game = Game(window, left_player, right_player, ball)
        game.main_loop()
    except (TclError, Terminator):
        pass


if __name__ == "__main__":
    main()
