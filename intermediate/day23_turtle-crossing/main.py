import random
import time
from turtle import Screen
from jerry import Jerry
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jerry = Jerry()

screen.listen()
screen.onkeypress(jerry.go_forward, "Up")
screen.onkeypress(jerry.go_backward, "Down")
screen.onkeypress(jerry.go_left, "Left")
screen.onkeypress(jerry.go_right, "Right")

cars = []

game_round = 0
sleep_time = 0.1
game_is_on = True
scoreboard = Scoreboard()

while game_is_on:

    time.sleep(sleep_time)
    screen.update()
    random_choice = random.randint(1, 6)
    if random_choice == 1:
        cars.append(Car())

    for car in cars:
        if jerry.distance(car) < 20:
            print(jerry.distance(car))
            game_is_on = False
        else:
            car.move()

    if jerry.ycor() > 300:
        scoreboard.gain_point()
        scoreboard.update_scoreboard()
        sleep_time *= 0.5
        jerry.go_home()

screen.exitonclick()
