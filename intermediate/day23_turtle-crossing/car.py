from turtle import Turtle
import random

class Car(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_len=2, stretch_wid=1)
    self.goto(300, random.randint(-250, 250))
    self.colors = ["red", "orange", "green", "blue", "purple"]
    self.color(random.choice(self.colors))

  def move(self):
    self.backward(10)
