import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class tharique:
    driver = webdriver.Chrome()
    url = 'https://www.imdb.com/search/title/'

    #select user by rating
    def select_user_by_rating(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_rating=self.driver.find_element(by=By.NAME,value='user_rating-min')
        time.sleep(2)
        user_rating.click()
        time.sleep(3)
    def display_per_page(self):
        user_rating=self.driver.find_element(by=By.NAME,value='user_rating-min')
        user_rating_dropdown=Select(user_rating)
        user_rating_dropdown.select_by_visible_text('10')
        user_display=self.driver.find_element(by=By.ID,value='search-count')
        user_display.click()
        time.sleep(3)
        display_dropdown=Select(user_display)
        display_dropdown.select_by_index('2')
        time.sleep(2)
    def Select_value_using_name_in_language(self):
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown=Select(language)
        language_dropdown.select_by_value('ab')
        time.sleep(3)
    def Select_value_using_visibleText(self):
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.select_by_visible_text('Aboriginal')
        time.sleep(3)
        language_dropdown.select_by_visible_text('Aché')
        time.sleep(3)
        language_dropdown.select_by_visible_text('Acholi')
        time.sleep(3)
    def deselect_values_using_value_and_visibleText(self):
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.deselect_by_value('ab')
        time.sleep(2)
        language_dropdown.deselect_by_visible_text('Aboriginal')
        time.sleep(2)
        language_dropdown.deselect_by_visible_text('Aché')
        time.sleep(3)
        language_dropdown.deselect_by_visible_text('Acholi')
        time.sleep(3)
    def select_all_values_in_language_dropdown(self):
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_options = language_dropdown.options
        print(language_options)
        for i in language_options:
            i.click()
    def Select_Movies_based_on_release_date(self):
        min_date = self.driver.find_element(by=By.NAME,value='release_date-min')
        time.sleep(2)
        min_date.send_keys("1990-01-01")
        max_date=self.driver.find_element(by=By.NAME, value='release_date-max')
        time.sleep(2)
        max_date.send_keys("1990-02-01")
        time.sleep(2)
    def click_searchButton(self):
        search_button = self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/p[3]/button')
        time.sleep(2)
        search_button.click()

am = tharique()
am.select_user_by_rating()
am.display_per_page()
am.Select_value_using_name_in_language()
am.Select_value_using_visibleText()
am.deselect_values_using_value_and_visibleText()
am.select_all_values_in_language_dropdown()
am.Select_Movies_based_on_release_date()
am.click_searchButton()



