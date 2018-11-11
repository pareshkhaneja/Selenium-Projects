from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path=r'C:\Users\pareshkhaneja\Downloads\Softwares\Selenium webdrivers\geckodriver-v0.22.0-win64\geckodriver')
baseURL="http://learn.letskodeit.com/p/practice"
driver.get(baseURL)
driver.maximize_window()
before_handle=driver.current_window_handle
print("Before click window handle"+before_handle)
driver.find_element_by_id("openwindow").click()
time.sleep(2)
handles=driver.window_handles
for handle in handles:
    if handle!=before_handle:
        driver.switch_to_window(handle)
        after_handle=driver.current_window_handle
        print("After click window Handle "+after_handle)