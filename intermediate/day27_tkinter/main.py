from tkinter import *
from tkinter import ttk

window = Tk()
window.minsize(width=500, height=300)
window.title("My First GUI Window!")
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(pady=20, padx=20)
sep = ttk.Separator(window, orient="horizontal")
sep.grid(row=3, column=0, columnspan=4, sticky="EW")
# Button
def button_click():
    my_label.config(text=field.get())


button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1, sticky="W")

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)


# "Entry" - AKA Single Line Text Field
field = Entry(width=10)
field.grid(column=3, row=2, sticky="W")

window.mainloop()
