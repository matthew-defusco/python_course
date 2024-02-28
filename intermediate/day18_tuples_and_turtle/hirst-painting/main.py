import random
import turtle as t
import colorgram

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.up()
tim.hideturtle()
tim.seth(225)
tim.forward(300)
tim.seth(0)

colors = []
for color in colorgram.extract("image.jpg", 30):
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors.append(new_color)


def random_color():
    return random.choice(colors)


def draw_row_of_dots():
    for _ in range(10):
        tim.dot(20, random_color())
        tim.forward(50)


for _ in range(10):
    draw_row_of_dots()
    tim.back(500)
    tim.left(90)
    tim.forward(50)
    tim.rt(90)


screen = t.Screen()
screen.exitonclick()
