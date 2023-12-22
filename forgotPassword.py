# 6. Verify that clicking the 'Forgot Password' link redirects the user to the password recovery page.

import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# script to navigate login url
driver.get("https://rahulshettyacademy.com/client/")

# script to maximize window
driver.maximize_window()

# script to navigate forgot password link
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

time.sleep(5)
# script to identify password recovery link
print(driver.current_url)

driver.close()