from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("C:/**ThePathWheretheDriverIs**/chromedriver.exe")
driver.get("https://linkedin.com")

time.sleep(4)

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("**YourUserName@ADomain.com**")
password.send_keys("**YourLinkedinPassword**")

time.sleep(4)

password = driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(4)



driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME,"buttons")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

message_buttons[0].click()
