import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/it_frequency.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, timer_id
    root.after_cancel(timer_id)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_title, text="Italian", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["italian"], fill="black")
    card_canvas.itemconfig(canvas_background, image=front_card_image)
    timer_id = root.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(canvas_background, image=back_card_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["english"], fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ----------------------- UI SETUP -------------------------- #
root = Tk()
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer_id = root.after(3000, flip_card)
#   Card Config   #
card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
canvas_background = card_canvas.create_image(400, 263, image=front_card_image)
card_title = card_canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = card_canvas.create_text(400, 263, font=("Arial", 70, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

#   Button Config   #
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
wrong_button = Button(image=wrong_image, bd=0, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=next_card)
right_button = Button(image=right_image, bd=0, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=is_known)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# -------------- GAME PLAY ------------------------ #

next_card()

root.mainloop()
