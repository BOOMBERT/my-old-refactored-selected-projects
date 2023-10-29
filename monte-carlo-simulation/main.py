import turtle
from random import randint
from math import sqrt
from time import sleep

#===WINDOW===
wn = turtle.Screen()
wn.setup(500,500)
wn.bgcolor('black')
wn.title('Number pi by method - Monte Carlo')

#===START_OPTIONS===
turtle.speed(0)
turtle.ht()
running = True

#===TEMPLATE===
def board():
    def square():
        turtle.color('blue')
        for i in range(4):
            turtle.forward(200)
            turtle.left(90)
    square()

    def circle():
        turtle.color('white')
        turtle.circle(100)
    turtle.pu()
    turtle.goto(100, 0)
    turtle.pd()
    circle()

board()

#===INFORMATION===
def writing():
    turtle.color('blue')
    turtle.up()
    turtle.goto(-225,175)
    turtle.write('Number:', font=("normal", 15, "normal"))

    turtle.goto(-225,125)
    turtle.write('Green points:', font=("normal", 12, "normal"))

    turtle.goto(-225,75)
    turtle.write('Red points:', font=("normal", 12, "normal"))

    turtle.goto(-225,25)
    turtle.write('All points:', font=("normal", 12, "normal"))

writing()

#===MAIN_PROGRAM===
def main():
    n = m = 0
    while running:
        #===RANDOM===
        x, y = randint(0,200), randint(0,200)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()

        #===CALCULATIONS===
        m += 1
        if (sqrt((x-100)**2 + (y-100)**2)) <= 100:
            turtle.dot(2, 'green')
            n += 1
        else:
            turtle.dot(2, 'red')
        number_pi = (n * 4) / m

        # ===HELPFUL_TURTLE===
        turtle2 = turtle.Turtle()

        # ===DISPLAYING_ALL_DATA===
        def display():
            #===HELPFUL_TURTLE_SETTINGS===
            turtle2.ht()
            turtle2.speed(0)
            turtle2.color('white')
            turtle2.up()

            turtle2.goto(-225, 150)
            turtle2.write(number_pi, font=("normal", 15, "normal"))

            turtle2.goto(-225, 100)
            turtle2.write(n, font=("normal", 15, "normal"))

            turtle2.goto(-225, 50)
            turtle2.write(m - n, font=("normal", 15, "normal"))

            turtle2.goto(-225, 0)
            turtle2.write(m, font=("normal", 15, "normal"))

        display()
        sleep(0.2)
        turtle2.clear()

try: main()
except turtle.Terminator: running = False