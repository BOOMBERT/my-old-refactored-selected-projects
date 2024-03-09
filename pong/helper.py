from turtle import Turtle

def to_px(value: float) -> float:
    DIFFERENCE_TO_PIXELS = 2 * 10
    return value * DIFFERENCE_TO_PIXELS

def turtle_setup(color: str) -> Turtle:
    local_turtle = Turtle()
    local_turtle.color(color)
    local_turtle.penup()
    local_turtle.speed(0)

    return local_turtle
