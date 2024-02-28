from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(coords=(350, 0))
l_paddle = Paddle(coords=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

r_score = 0
l_score = 0

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        sleep_time *= 0.9
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_time *= 0.9

    if ball.xcor() > 390 or ball.xcor() < -390:
        sleep_time = 0.1
        if ball.xcor() > 390:
            scoreboard.l_point()
        else:
            scoreboard.r_point()
        ball.home()
        ball.bounce_x()
        ball.move()


screen.exitonclick()
