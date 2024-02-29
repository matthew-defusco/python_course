import time
from turtle import Screen
from jerry import Jerry
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jerry = Jerry()
car_manager = CarManager()

screen.listen()
screen.onkeypress(jerry.go_forward, "Up")
screen.onkeypress(jerry.go_backward, "Down")
screen.onkeypress(jerry.go_left, "Left")
screen.onkeypress(jerry.go_right, "Right")

game_round = 0
sleep_time = 0.1
game_is_on = True
scoreboard = Scoreboard()

while game_is_on:

  time.sleep(sleep_time)
  screen.update()

  car_manager.create_car()
  car_manager.move_cars()
  # if game_round % 6 == 0:
  #   cars.append(Car())
  #   cars.append(Car())
  #   game_round = 0
  #
  # for car in cars:
  #   if jerry.distance(car) < 20:
  #     print(jerry.distance(car))
  #     game_is_on = False
  #   else:
  #     car.move()
  #
  # if jerry.ycor() > 300:
  #   scoreboard.gain_point()
  #   scoreboard.update_scoreboard()
  #   sleep_time *= 0.85
  #   jerry.go_home()
  #
  # game_round += 1


screen.exitonclick()
