from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button.btn")

first_name.send_keys("Matthew")
last_name.send_keys("DeFusco")
email.send_keys("asdf@asdf.com")
sign_up_button.click()

# driver.quit()
