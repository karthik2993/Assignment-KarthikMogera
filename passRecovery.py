
#7. Validate the password recovery functionality by following these steps:
#a. Click the 'Forgot Password' link.
#b. Enter a registered email address in the provided field.
#c. Click the 'Recover Password' button.
#d. Verify that a success message is displayed indicating that an email with password recovery instructions          has been sent.
#e. Simulate the password recovery process by accessing the provided email or using a test email account.
#f. Retrieve the recovery instructions and follow the specified steps to reset the password.
#g. Ensure that after successfully resetting the password, the user is redirected to the login page.
#h. Validate that the user can log in with the new password.


import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# script to navigate login url
driver.get("https://practice.automationtesting.in/my-account/")

# script to maximize window
driver.maximize_window()

# script to navigate forgot password link
driver.find_element(By.LINK_TEXT, "Lost your password?").click()

time.sleep(5)
# script to identify password recovery link
print(driver.current_url)
loginid = "karthikaffiliate29@gmail.com"
# script to enter recovery email id
driver.find_element(By.ID, "user_login").send_keys(loginid)
time.sleep(5)

# script to click on reset button
driver.find_element(By.XPATH, "//input[@value='Reset Password']").click()

# script to read recovery instructions
message = driver.find_element(By.XPATH, "//div/p[contains(text(),'A password reset email')]").text

print(message)

# script for redirecting to login page
driver.find_element(By.LINK_TEXT, "My Account").click()

# script to verify whether user logged in successfully after reset
driver.find_element(By.NAME, "username").send_keys(loginid)

driver.find_element(By.NAME, "password").send_keys("Ashkar$29")

driver.find_element(By.NAME, "login").click()

details = driver.find_element(By.XPATH, "//div/p").text

# assertion method to check post login
assert "karthikaffiliate29" in details


driver.close()
