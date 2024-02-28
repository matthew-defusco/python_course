from turtle import Turtle

class Jerry(Turtle):
  def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
    super().__init__(shape, undobuffersize, visible)
    self.penup()
    self.go_home()

  def go_home(self):
    self.goto(0, -280)
    self.seth(90)

  def go_forward(self):
    self.fd(10)

  def go_backward(self):
    self.back(10)

  def go_left(self):
    self.goto(self.xcor() - 10, self.ycor())

  def go_right(self):
    self.goto(self.xcor() + 10, self.ycor())
