import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options_1 = Options()
options_1.headless = True

driver_chrome = webdriver.Chrome(options=options_1)
#url = "https://www.google.co.in/"
#driver_chrome.get(url)

class Program:
    def __init__(self, url):
        self.url=url
        driver_chrome.get(self.url)
    def get_title(self):
        print(driver_chrome.title)
    def get_url(self):
        print(driver_chrome.current_url)

url_1 = "https://www.guvi.in"
prog = Program(url_1)
prog.get_title()
prog.get_url()
driver_chrome.quit()