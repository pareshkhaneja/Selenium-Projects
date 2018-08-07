from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeTest():
    
    def get():
        #Instantiate chrome browser 
        driver=webdriver.Chrome()
        
        #Open provided URL
        driver.get("https://learn.letskodeit.com/p/practice")
        if "Practice | Let's Kode It" in driver.title:
            print("Website successfully opened.")
        else:
            print("Website couldn't get opened.")
            driver.close()
            
chrome = ChromeTest()
chrome.get()
    
