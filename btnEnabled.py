#5. Confirm that the 'Login' button is enabled only when both username and password fields are filled with valid input.


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# script to navigate login url
driver.get("https://training.openspan.com/login")

driver.find_element(By.ID,"user_name").send_keys("ABCD")

driver.find_element(By.ID,"user_pass").send_keys("1234")

# Script to verify whether login button is enabled or not if true means button is in enabled state
print(driver.find_element(By.ID, "login_button").is_enabled())


driver.close()