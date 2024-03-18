import json
import secrets
import string
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(20))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Not enough info", message="You must fill in all the fields.")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                # Write that data back to the file
                json.dump(new_data, file, indent=2)
        else:
            # Update that data
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                # Write that data back to the file
                json.dump(data, file, indent=2)
        finally:
            website_entry.focus()
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORDS ---------------------------#
def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            password_data = json.load(file)[website]
    except FileNotFoundError:
        messagebox.showerror(message="There are no passwords saved yet!")
    except KeyError:
        messagebox.showerror(title="Nope", message="There's no password saved for that website.")
    else:
        messagebox.showinfo(title="Password info", message=f"Website: {website}\n"
                                                           f"Email: {password_data["email"]}\n"
                                                           f"Password: {password_data["password"]}")

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("MyPass")
root.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1, columnspan=2)

# Components
website_label = Label(text="Website:")
website_entry = Entry(width=21)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_entry.insert(0, "matthew.defusco@gmail.com")

password_label = Label(text="Password:")
password_entry = Entry(width=21)

generate_button = Button(text="Generate Password", command=create_password)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", width=13, command=search)

# Layout
website_label.grid(row=1, column=0, sticky="E")
website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_label.grid(row=2, column=0, sticky="E")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_label.grid(row=3, column=0, sticky="E")
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

root.mainloop()
