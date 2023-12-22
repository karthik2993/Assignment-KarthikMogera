# Check the strength of the password and validation messages for the same.

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.uic.edu/apps/strong-password/")

# script to enter password
driver.find_element(By.ID, "passwordPwd").send_keys("Ash$123@")

# script to check strength of password and validation message
strength = driver.find_element(By.XPATH, "//p[@id='complexity']").text

print("Password strength:",strength)
