from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(width=300, height=300)
root.title("Miles to Km Converter")
root.config(pady=100, padx=50)

# Show a field for a user to enter a number in "miles" to convert
distance_to_convert = Entry(width=4, justify="center")
distance_to_convert.insert(END, string="0")
distance_to_convert.grid(row=0, column=1)

# Show a label for the field
miles_label = Label(text="miles")
miles_label.grid(row=0, column=2)

# Show a label for the conversion sentence start
equals = Label(text="is equal to")
equals.grid(row=1, column=0)

# Show a label that is dependent on the conversion
converted_distance = Label(text=0)
converted_distance.grid(row=1, column=1)

# Show km label
km_label = Label(text="km")
km_label.grid(row=1, column=2)


# Create a button that, when clicked, does the conversion
def convert():
    converted_distance.config(text=int(distance_to_convert.get()) * 1.609)


convert_button = Button(text="Calculate", command=convert)
convert_button.grid(row=2, column=1)

root.mainloop()
