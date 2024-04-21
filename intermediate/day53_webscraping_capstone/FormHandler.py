import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class FormHandler:
  def __init__(self) -> None:
    self.options = webdriver.ChromeOptions()
    self.options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(self.options)


  def init(self, form_url):
    self.driver.get(form_url)
    time.sleep(2)

  def fill_form(self, address, price, link):
    address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = self.driver.find_element(By.CSS_SELECTOR, value='div[role="button"]')

    address_input.send_keys(address)
    # time.sleep(1)
    price_input.send_keys(price)
    # time.sleep(1)
    link_input.send_keys(link)
    # time.sleep(1)

    submit_button.click()

  def reset_form(self):
    self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    # time.sleep(2)

  def teardown(self):
    self.driver.quit()

