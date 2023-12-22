
#8. Account for pagination on the login page and the script to automatically navigate through multiple pages, ensuring that all relevant data is captured.
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# script to navigate login url
driver.get("https://practice.automationtesting.in/my-account/")
loginid = "karthikaffiliate29@gmail.com"
# script to maximize window
driver.maximize_window()

# Script to enter email id
driver.find_element(By.NAME, "username").send_keys(loginid)

# Script to enter password

driver.find_element(By.NAME, "password").send_keys("Ashkar$29")

# Script to enter email id
driver.find_element(By.NAME, "login").click()

# script to click another page

driver.find_element(By.LINK_TEXT, "Shop").click()

time.sleep(5)
# script to validate whether is redirected to correct page
msg = driver.find_element(By.XPATH, "//nav[@class='woocommerce-breadcrumb']").text

print(msg)

time.sleep(5)

# script to navigate another page
driver.find_element(By.LINK_TEXT, "AT Site").click()

# This script identifies whether it is landed to correct page
item = driver.find_elements(By.XPATH, "//a[@class='ui builder_button default']")

for items in item:
    print(items.text)

driver.close()
