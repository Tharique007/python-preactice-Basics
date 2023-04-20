from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class haneef:
    driver=webdriver.Chrome()

    def __init__(self,url):
        self.url=url

    def Alert_box(self):
        self.driver.get(self.url)
        alert_button=self.driver.find_element(by=By.XPATH,value='/html/body/form/input')
        time.sleep(4)
        alert_button.click()

url = "file:///D:/Guvi/index.html"

han = haneef(url)
han.Alert_box()