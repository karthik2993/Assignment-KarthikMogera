#3. Ensure that the login page retains the entered username and password fields' values after a failed login attempt.

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

# script to enter email

driver.find_element(By.XPATH, "//form/div[1]//input[@type='email']").send_keys("karthikmogera@gmail.com")

# script to enter password
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("11")

# script to click on login button
driver.find_element(By.ID, "login").click()

time.sleep(5)

username=driver.find_element(By.ID,"userEmail").text
print(username)


driver.close()