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

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Not enough info", message="You must fill in all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Website: {website}\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}")

        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.focus()
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
website_entry = Entry(width=35)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_entry.insert(0, "matthew.defusco@gmail.com")

password_label = Label(text="Password:")
password_entry = Entry(width=21)

generate_button = Button(text="Generate Password", command=create_password)
add_button = Button(text="Add", width=36, command=save)

# Layout
website_label.grid(row=1, column=0, sticky="E")
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_label.grid(row=2, column=0, sticky="E")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_label.grid(row=3, column=0, sticky="E")
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

root.mainloop()
