from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #starts the webdriver
driver.get("https://linkedin.com")

time.sleep(4)

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("MyUsername")   #insert you username to access to Linkedin
password.send_keys("MyPassword")  #insert you passowrd to access to Linkedin

time.sleep(4)

submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(4)


# *** Add to the next line the page where you want to start to send messages, as it is it will start from recently added connection
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME,"button")
message_buttons =  [btn for btn in all_buttons if "Message" in btn.text]
time.sleep(2)

# the following for loop is potentially infinite and is going to write to all your contact, so keep an eye on it.
for i in range(0, len(message_buttons)):

    message_buttons[i].click()
    time.sleep(2)
    main_div = driver.find_element(By.XPATH,"//div[starts-with(@class, 'msg-form__msg-content-container')]")
    driver.execute_script("arguments[0].click();",main_div)
    paragraphs = driver.find_elements(By.TAG_NAME,"p")
    # Please personalize your message between the " "
    paragraphs[-5].send_keys("Thank you for accepting my connection request!")

    time.sleep(4)

    #after you have changed the message and the login data you can delete the # in the following two line and execute the bot
    #submit = driver.find_element(By.XPATH,"//button[@type='submit']")
    #driver.execute_script("arguments[0].click();",submit)


    time.sleep(2)


    close_button = driver.find_element(By.XPATH,"//button[@class = 'msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']")
    driver.execute_script("arguments[0].click();",close_button)

    time.sleep(4)

