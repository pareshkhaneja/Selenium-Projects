from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://learn.letskodeit.com/p/practice")
if "Practice | Let's Kode It" in driver.title:
    print("Website successfully opened.")
else:
    print("Website couldn't get opened.")

try:
    element=driver.find_element_by_id("name")           #This function locates element by id.
    print("Element by id has been located")
except:
    print("Element couldn't be found.")

driver.close()