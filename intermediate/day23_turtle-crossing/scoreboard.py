from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-280, 270)
    self.score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score}", False, "left", ("Courier", 20, "normal"))

  def gain_point(self):
    self.score += 1