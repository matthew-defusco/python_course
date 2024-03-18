import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name:")
    if answer_state in state_data["state"].values:
        x_cor = state_data[state_data["state"] == answer_state]["x"].iloc[0]
        y_cor = state_data[state_data["state"] == answer_state]["y"].iloc[0]
        state_name = State(answer_state, x_cor, y_cor)
        state_name.write_state_name()
        correct_guesses.append(state_name)
    elif answer_state is None:
        break
    else:
        print("Nope")


screen.exitonclick()
