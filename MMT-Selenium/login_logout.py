from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
import getpass

print("\nWelcome to MMT(Make My Trip) Autobot\nThis bot will test the following features of MMT website:\n1.Login and Logout.\n2.Flight Search.\n3.Hotel Search.\n")
email=raw_input("In order to continue further, please enter your credentials to get access to MMT website.\nEmail Address: ")
passwd=getpass.getpass("Password: ")
print("Please have patience while we come up with results...")
driver = webdriver.Firefox(executable_path = 'C:\Users\Home\Downloads\geckodriver-v0.21.0-win64\geckodriver.exe')
driver.get("https://www.makemytrip.com")
    #print(driver.title)
driver.find_element_by_css_selector('a#ch_login_icon').click()
driver.find_element_by_css_selector('input#ch_login_email').send_keys(email)        #Locating email address text box and sending inputs
driver.find_element_by_css_selector('input#ch_login_password').send_keys(passwd)    #Locating password text box and sending inputs
driver.find_element_by_id('ch_login_btn').click()        #Locating and clicking Log-in button
driver.find_element_by_css_selector('span[mt-id="username"]')
print("Login Successful!")

logout=driver.find_element_by_css_selector('span[mt-id="username"]').submit()
action=ActionChains(driver)
action.move_to_element(logout)
driver.find_element_by_xpath("//a[contains(text(),'Logout')]")
print("Logged out!")



