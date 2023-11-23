# import turtle
# tim = turtle.Turtle()

import random
# from turtle import Turtle, Screen

import turtle as t  # (t = alias)
tim = t.Turtle()
t.colormode(255)

# Drawing a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Dashed Walk
# for _ in range(15):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)


def random_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    color = (r, g, b)
    return color


# Drawing one polygon inside another
# for sides in range(3, 10):
#     tim.pencolor(random_color())
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)

# Random Walk
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
