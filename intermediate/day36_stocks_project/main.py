import requests
import os
import smtplib
from email.mime.text import MIMEText


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": STOCK_API_KEY
# }
# stock_response = requests.get(STOCK_ENDPOINT, params=parameters)
# stock_response.raise_for_status()
#
# stock_data = [{key: value} for (key, value) in stock_response.json()["Time Series (Daily)"].items()]
# print(stock_data)
# # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# # TODO 2. - Get the day before yesterday's closing stock price
# daily_values = [list(day.values())[0]["4. close"] for day in stock_data]
#
# # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# daily_diff = float(daily_values[0]) - float(daily_values[1])
# # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
# #  before yesterday.
# daily_diff_percent = (abs(daily_diff) / float(daily_values[0])) * 100
#
# # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if daily_diff_percent > 5:
#     print("Get news")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_parameters = {
    "apiKey": "33e334e40bc6463d983ef6245d9e8f02",
    "q": COMPANY_NAME
}
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
#  https://stackoverflow.com/questions/509211/understanding-slice-notation
articles_list = news_response.json()["articles"][:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
content = [{"headline": article["title"], "description": article["description"].replace("\n", "")} for article in articles_list]
# FOR TESTING ONLY
daily_diff = -5
daily_diff_percent = 5
up_or_down = ""
if daily_diff > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"
formatted_content = f"""
{STOCK_NAME}: {up_or_down} {daily_diff_percent} \n
"""


for article in content:
    article["headline"].replace("\n", "")
    article["description"].replace("\n", "")
    headline = article["headline"] + "\n"
    description = article["description"] + "\n"
    formatted_content += headline + description + "\n"

print(formatted_content)
# TODO 9. - Send each article as a separate message via Email.
my_email = "dev.testing.5878@gmail.com"
password = "chhtiosxcnzezios"

test_receiver = "dev.testing5878@yahoo.com"

send_string = MIMEText(formatted_content.encode("utf-8"), _charset="utf-8")
send_string["Subject"] = "Subject: Your stock info!"
send_string["From"] = my_email
send_string["To"] = test_receiver

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(send_string)
    connection.close()

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=test_receiver,
#         msg=f"Subject: Your stock info!\n\n{send_string}"
#     )
#     connection.close()

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
