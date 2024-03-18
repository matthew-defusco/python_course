import random
import smtplib
import datetime as dt

MY_EMAIL = "dev.testing.5878@gmail.com"
MY_PASSWORD = "chhtiosxcnzezios"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(MY_EMAIL, "matthew.defusco@gmail.com", f"Subject: Be positive you sad sack of shit!\n\n{quote}")