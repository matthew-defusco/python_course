from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Setting these two options allows you to get around the Captchas on a website after the initial run
chrome_options.add_argument("--user-data-dir=/Users/matthewdefusco/Library/Application Support/Google/Chrome/Default")
chrome_options.add_argument("--profile-directory=SeleniumProfile")

driver = webdriver.Chrome(chrome_options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is: {price_dollar}.{price_cents}")

driver.get("https://www.python.org/")
search = driver.find_element(By.NAME, value="q").tag_name
button = driver.find_element(By.ID, value="submit").text
print(f"Search bar tag name: {search}, search button text: {button}")

docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").get_attribute("href")
print(f"Docs link href value: {docs_link}")

bug_report = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a').text
print(f"Bug report link text found with XPath: {bug_report}")


driver.quit()
