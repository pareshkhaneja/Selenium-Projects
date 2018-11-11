from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path=r'C:\Users\pareshkhaneja\Downloads\Softwares\Selenium webdrivers\geckodriver-v0.22.0-win64\geckodriver')
baseURL="http://learn.letskodeit.com/p/practice"
driver.get(baseURL)
driver.maximize_window()
driver.switch_to.frame("courses-iframe")
time.sleep(2)
print("Switched to iFrame")
driver.find_element_by_id("search-courses").send_keys("Success!")

