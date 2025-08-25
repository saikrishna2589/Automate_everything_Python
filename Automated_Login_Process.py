# Step 1: create a Chrome driver with customised settings as to how you want to open the browser
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import os
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

from datetime import datetime

#load variables from .env file in current directory
load_dotenv()
env= os.getenv("python_automated")

#make directory for storing files every 2 seconds.
os.makedirs("temp_readings" , exist_ok = True)


def get_driver():
#set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features = AutomationContolled")
    driver =webdriver.Chrome(options= options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver



#login and go to the home screen
print()
def login():
    driver_call.find_element(by= "id" , value ="id_username").send_keys("automated")
    #login username ='automated'
    time.sleep(2)
    driver_call.find_element(by="id", value ="id_password").send_keys(env + Keys.RETURN) #activate driver and send keys
    time.sleep(2)
    driver_call.find_element(by="xpath" , value = "/html/body/nav/div/a").click()
    print(driver_call.current_url)
    time.sleep(5)


#clean the extracted text
def cleaned_text(text):
    cleaned_data = text.split(": ")
    cleaned_data = float(cleaned_data[1])
    return cleaned_data

def current_datetime():
    current_datetime_now = datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
    return current_datetime_now

# save the value into text file and return the file it wrote to
def save_file(value):
    path = f"temp_readings/{current_datetime()}.txt"
    with open(path,'w') as file:
        print("about to write:", value, type(value))
        file.write(str(value))
        return f"successfully wrote {value} to {path}"



 # purpose of extract_info() : extract the temperature and return only the float.
def extract_info():
    #calling login() function
    time.sleep(2)
    temp_info = driver_call.find_element(by ="xpath" , value ="/html/body/div[1]/h1[2]" )
    cleaned_data = cleaned_text(temp_info.text)  #calling cleaned_text function
    return float(cleaned_data)

driver_call = get_driver()  #loads chrome driver with options
login()  #login and click on home button

temp = extract_info()
print(f"{save_file(temp)}")
#save_file(extract_info()) #save extract value to file
#schedule every 2 seconds the run. saves each data point in text file .each text file name-currentdatetime
#(2025-08-21.13.50.59.txt)

try:
    while True:
        time.sleep(2)
        driver_call = get_driver()
        login()
        save_file(extract_info())

except KeyboardInterrupt:
    print("stopped")

finally:
    driver_call.quit() #close browser cleanly










