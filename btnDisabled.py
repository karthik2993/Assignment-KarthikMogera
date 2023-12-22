# 4. Test that the 'Login' button is disabled when both username and password fields are empty.

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# script to navigate login url
driver.get("https://training.openspan.com/login")

# Script to verify whether login button is enabled or not if False ,means button is in disbaled state
print(driver.find_element(By.ID, "login_button").is_enabled())


driver.close()