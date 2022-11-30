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

submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(4)



driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME,"buttons")
message_buttons =  [btn for btn in all_buttons if "Message" in btn.text]
time.sleep(2)


for i in range(0, len(message_buttons)):

    message_buttons[i].click()
    time.sleep(2)
    main_div = driver.find_element(By.XPATH,"//div[starts-with(@class, 'msg-form__msg-content-container')]")
    main_div.click()
    paragraphs = driver.find_elements(By.TAG_NAME,"p")
    paragraphs[-5].send_keys("This is a test message for linkedin automation")

    time.sleep(4)

    submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()

    time.sleep(2)


    close_button = driver.find_element(By.XPATH,"//button[@class = 'msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']")
    close_button.click()

    time.sleep(4)

