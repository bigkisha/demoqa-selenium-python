from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FormsPage(BasePage):
    PRACTICE_FORM_BUTTON = (By.XPATH, "//*[text()='Practice Form']/ancestor::*[contains(@id, 'item-')]")

    def click_practice_form_button(self):
        element = self.find_element(*self.PRACTICE_FORM_BUTTON)
        self.move_to_element(element)
        element.click()