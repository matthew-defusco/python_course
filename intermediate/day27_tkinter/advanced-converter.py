from tkinter import *

root = Tk()
root.minsize(width=200, height=300)
root.title("Miles to Km Converter")
root.config(pady=100, padx=50)


def calculate(*args):
    from_unit = from_unit_selection.get()
    to_unit = to_unit_selection.get()
    coverting_number = int(number_to_convert.get() or 0)
    if from_unit == to_unit:
        converted_number.config(text=coverting_number)
    elif from_unit == "mile":
        if to_unit == "km":
            converted_number.config(text=coverting_number * 1.609)
        elif to_unit == "meter":
            converted_number.config(text=coverting_number * 1609)
        elif to_unit == "foot":
            converted_number.config(text=coverting_number * 5280)
    elif from_unit == "km":
        if to_unit == "mile":
            converted_number.config(text=coverting_number / 1.609)
        elif to_unit == "meter":
            converted_number.config(text=coverting_number * 1000)
        elif to_unit == "foot":
            converted_number.config(text=coverting_number * 3281)
    elif from_unit == "meter":
        if to_unit == "mile":
            converted_number.config(text=coverting_number / 1609)
        elif to_unit == "meter":
            converted_number.config(text=coverting_number / 1000)
        elif to_unit == "foot":
            converted_number.config(text=coverting_number * 3.281)
    elif from_unit == "foot":
        if to_unit == "mile":
            converted_number.config(text=coverting_number / 5280)
        elif to_unit == "meter":
            converted_number.config(text=coverting_number * 304.8)
        elif to_unit == "km":
            converted_number.config(text=coverting_number / 3281)
    else:
        converted_number.config(text=coverting_number)


# Configure the options to convert to and from
conversion_options = ["mile", "foot", "km", "meter"]

# Set up the values where the "to" and "from" conversions will be stored and the number to convert variable
from_unit_selection = StringVar(value="mile")
to_unit_selection = StringVar(value="km")
number_to_convert_var = StringVar()

# Show a field for a user to enter a number to convert to another unit
number_to_convert = Entry(width=4, justify="center", textvariable=number_to_convert_var)
number_to_convert.insert(END, string="0")
number_to_convert_var.trace("w", calculate)
number_to_convert.grid(row=0, column=0)

# Show a selector for the user to choose which units to convert from
from_dropdown = OptionMenu(root, from_unit_selection, *conversion_options, command=calculate)
from_dropdown.grid(row=0, column=1)

# Show the equals symbol
equals_symbol = Label(text="=", font=('Helvetica', 20))
equals_symbol.grid(row=1, column=0, columnspan=2)

# Show a field for a user to enter a number to convert to another unit
converted_number = Label(text="0", width=4, justify="center")
converted_number.grid(row=2, column=0)

# Show a selector for the user to choose which units to convert to
to_dropdown = OptionMenu(root, to_unit_selection, *conversion_options, command=calculate)
to_dropdown.grid(row=2, column=1)

root.mainloop()
