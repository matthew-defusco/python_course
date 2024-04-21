import time
import requests
from bs4 import BeautifulSoup
import lxml

from FormHandler import FormHandler

FORM_LINK = "https://forms.gle/eGuy7rhwjSQ4wX368"

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "lxml")

listings = soup.select('article[data-test="property-card"]')

prices = [home.select_one('span[data-test="property-card-price"]')
          .text
          .strip()
          .split("+")[0]
          .replace("/mo", "")
          for home in listings]

links = [home.select_one('a[data-test="property-card-link"]').get("href") for home in listings]

addresses = [home.select_one('address[data-test="property-card-addr"]').text.replace("|", "").strip() for home in listings]

# time.sleep(4)

form = FormHandler()

form.init(FORM_LINK)

for i in range(len(listings)):
  form.fill_form(address=addresses[i], price=prices[i], link=links[i])
  form.reset_form()

form.teardown()
