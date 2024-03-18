import os
import random
import datetime as dt
import smtplib
import pandas


MY_EMAIL = "dev.testing.5878@gmail.com"
MY_PASSWORD = "chhtiosxcnzezios"

today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
letters = []

files = os.listdir("letter_templates")

for file in files:
    if file.endswith(".txt"):
        with open("letter_templates/" + file, "r") as letter:
            text = letter.read()
            letters.append(text)


for index, row in data.iterrows():
    name = row["name"]
    email = row["email"]
    birthday_month = row["month"]
    birthday_day = row["day"]

    if today.month == birthday_month and today.day == birthday_day:
        letter_text = random.choice(letters)
        letter_to_send = letter_text.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(MY_EMAIL, "matthew.defusco@gmail.com", f"Subject: Happy Birthday!\n\n{letter_to_send}")
