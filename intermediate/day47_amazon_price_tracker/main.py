import os
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv

load_dotenv()

TARGET_PRICE = float(100)

headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.9,la;q=0.8"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

int_price = soup.select_one("span.a-price-whole").get_text()
decimal_price = soup.select_one("span.a-price-fraction").get_text()
whole_price = float(int_price+decimal_price)

if whole_price <= TARGET_PRICE:
  text_to_send = f"Wow! The thing you wanted to track is cheaper than $100 now! Go check it out!!"
  send_string = MIMEText(text_to_send.encode("utf-8"), _charset="utf-8")
  send_string["To"] = "dev.testing5878@yahoo.com"
  send_string["Subject"] = "Subject: New price alert on Amazon!"

  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(
      user="dev.testing.5878@gmail.com",
      password=os.environ["EMAIL_PASSWORD"]
    )
    connection.send_message(send_string)
    connection.close()
