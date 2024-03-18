# import smtplib
#
# my_email = "dev.testing.5878@gmail.com"
# password = "chhtiosxcnzezios"
#
# test_receiver = "dev.testing5878@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=test_receiver,
#         msg="Subject: This is for you!\n\nHello!")
#     connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# if year == 2024:
#     print("This will work because the year is an int!")
# print(year, day_of_week)
#
# date_of_birth = dt.datetime(year=1990, month=8, day=30)
# weekday_I_was_born = date_of_birth.weekday()
# print(date_of_birth, weekday_I_was_born)
