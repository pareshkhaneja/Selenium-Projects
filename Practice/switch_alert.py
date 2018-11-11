from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path=r'C:\Users\pareshkhaneja\Downloads\Softwares\Selenium webdrivers\geckodriver-v0.22.0-win64\geckodriver')
baseURL="http://learn.letskodeit.com/p/practice"
driver.get(baseURL)
driver.maximize_window()
driver.find_element_by_id("name").send_keys("Paresh")
driver.find_element_by_id("alertbtn").click()
time.sleep(2)
alert1=driver.switch_to.alert
alert1.accept()
print("Switched to alert")
driver.find_element_by_id("name").send_keys("Paresh")
driver.find_element_by_id("confirmbtn").click()
time.sleep(2)
alert1=driver.switch_to.alert
alert1.accept()
driver.quit()
