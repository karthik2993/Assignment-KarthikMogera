
# 1. Verify that a user with valid credentials can successfully log in and access the system.


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
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Ashkar$29")

# script to click on login button
driver.find_element(By.ID, "login").click()

time.sleep(5)

# script to verify whether user logged in successfully or not
message = driver.find_element(By.XPATH, "//button[normalize-space()='HOME']").text

print(message)

if message == "HOME":
    print("Logged in successfully")
else:
    print("Login failure")
