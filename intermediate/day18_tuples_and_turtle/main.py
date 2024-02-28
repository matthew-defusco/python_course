import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# DRAWING SHAPES WITH DIFFERENT NUMBER OF SIDES
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.pencolor()
#         tim.right(360 / num_sides)
#         tim.fd(100)
#
#
# for shape_side_n in range(3, 11):
#     tim.pencolor(random.choice(colors))
#     draw_shape(shape_side_n)

# DRAWING A RANDOM WALK
# for _ in range(100):
#     tim.speed("fastest")
#     tim.pensize(10)
#     tim.color(random_color())
#     direction = random.choice([0, 90, 180, 270])
#     tim.setheading(direction)
#     tim.fd(30)

# DRAWING A SPIROGRAPH
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    heading = 0
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        heading += size_of_gap
        tim.seth(heading)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
