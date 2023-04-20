from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
class tharique:


    def __init__(self, url):
        self.url = url
        driver.get(self.url)
    def find_id(self, id):
        try:
            driver.find_element(By.ID, value=id)
            time.sleep(6)
            driver.find_element(By.ID, value=id).click()
        except:
            print("the HTML id does not exist ")

    def close_button(self,class_name):
        try:
            time.sleep(6)
            driver.find_element(By.CLASS_NAME, value=class_name).click()
        except:
            print("cclass id does not exist")

    def ancor_tag(self,id,ancor_text):
        try:
            driver.find_element(By.ID, value=id).click()
            time.sleep(6)
            driver.find_element(By.LINK_TEXT, value=ancor_text).click()
        except:
            print("ancor link is not available")

class guvi:
    def __init__(self, url):
        self.url = url
        driver.get(self.url)
    def login_button(self,key):
        try:
            time.sleep(6)
            driver.find_element(By.LINK_TEXT, value=key).click()
        except:
            print("no class")



url ="https://www.w3schools.com/"
id="w3loginbtn"
class_name="TopBarMenuLegacy_user_profile_button__xiNV9"
anco_text="W3schools"

#thq = tharique(url)
#thq.find_id(id)
#thq.close_button(class_name)
#thq.ancor_tag(id,anco_text)

url_1="https://www.guvi.in/"
key_1="Login"
gv=guvi(url_1)
gv.login_button(key_1)