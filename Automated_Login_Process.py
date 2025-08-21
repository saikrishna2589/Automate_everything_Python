# Step 1: create a Chrome driver with customised settings as to how you want to open the browser
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import os
import time
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv


#load variables from .env file in current directory
load_dotenv()
env= os.getenv("python_automated")


def get_driver():
#set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features =  AutomationContolled")
    driver =webdriver.Chrome(options= options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


driver_call = get_driver()
def login():
    driver_call.find_element(by= "id" , value ="id_username").send_keys("automated")
    #login username ='automated'
    time.sleep(2)
    driver_call.find_element(by="id", value ="id_password").send_keys(env + Keys.RETURN)
    time.sleep(2)
    driver_call.find_element(by="xpath" , value = "/html/body/nav/div/a").click()
    print(driver_call.current_url)
    time.sleep(5)

def cleaned_text(text):
    cleaned_data = text.split(": ")
    cleaned_data = float(cleaned_data[1])
    return cleaned_data

def extract_info():
    login()
    time.sleep(2)
    temp_info = driver_call.find_element(by ="xpath" , value ="/html/body/div[1]/h1[2]" )
    return cleaned_text(temp_info.text)


print(extract_info())

