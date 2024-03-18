from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__(visible=False)
        self.penup()
        self.setx(x)
        self.sety(y)
        self.state = state

    def write_state_name(self):
        self.write(self.state, align="center", font=("Courier", 15, "normal"))
