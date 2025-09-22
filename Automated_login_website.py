#packages

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#we are trying to login into titan 22
from selenium.webdriver.common.by import By

import time
def get_driver():
#set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationContolled")
    driver =webdriver.Chrome(options= options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


#Login
def login():
    driver_call = get_driver()
    time.sleep(5)
    driver_call.find_element(By.ID, value='CustomerEmail').send_keys('datahaveninbox@gmail.com')

    time.sleep(5)
    (driver_call.find_element(By.ID, value='CustomerPassword')
     .send_keys('furyfury2525'+ Keys.RETURN))


    print(driver_call.current_url)

    time.sleep(10)

login()