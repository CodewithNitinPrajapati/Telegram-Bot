'''
Created on 05-May-2024

@author: nitin
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
user_name = "standard_user"
password = "secret_sauce"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
element = driver.find_element("id", "user-name")

element.send_keys(user_name)
print(user_name)
time.sleep(5)
element = driver.find_element("id","password")
element.send_keys(password)
print(password)
time.sleep(5)
element.submit()
time.sleep(5)
#element.send_keys(Keys.RETURN)
