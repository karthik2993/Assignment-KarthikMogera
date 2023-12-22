# 2. Validate that an error message is displayed when attempting to log in with invalid credentials.

import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# Script to navigate login page
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()

# Script to enter username
driver.find_element(By.ID, "username").send_keys("student")

# Script to enter password
driver.find_element(By.NAME, "password").send_keys("11")

# Script to click on login button
driver.find_element(By.ID, "submit").click()
time.sleep(5)

# Script to read error message for invalid credential
errmsg = driver.find_element(By.XPATH, "//div[@id='error']").text

# script print login failure message
print("Login Failure message", errmsg)


driver.close()