import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Pick a color: ")

colors = ["red", "orange", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# for color in colors:
#     turtle = Turtle(shape="turtle")
#     turtle.color(color)
#     turtle.penup()
#     turtle.goto(x=x, y=y)
#     y += 50

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if bet == winning_color:
                print(f"You win! The winning color was {winning_color}.")
            else:
                print(f"Sorry, you lost! You guessed {bet} but the winning color was {winning_color}.")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
