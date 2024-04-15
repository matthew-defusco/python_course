from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://www.python.org/")

event_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

new_dict = {i: {'name': event_list[i].text, 'date': event_dates[i].text} for i in range(len(event_list))}
print(new_dict)


driver.quit()