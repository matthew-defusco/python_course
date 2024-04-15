import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

timeout = time.time() + 30
five_seconds = time.time() + 5

def check_store():
  """Checks the store every 5 seconds and returns the most expensive item from the store if there is one."""
  active_store_items = driver.find_elements(By.CSS_SELECTOR, value="div#store div:not(.grayed) b")
  if len(active_store_items) == 0:
    return None
  else:
    return active_store_items[-1]

while True:
  cookie.click()
  if time.time() > timeout:
    print(driver.find_element(By.ID, value="cps").text)
    driver.quit()
    break
  elif time.time() > five_seconds:
    result = check_store()
    if result is not None:
      result.click()
    five_seconds = time.time() + 5
