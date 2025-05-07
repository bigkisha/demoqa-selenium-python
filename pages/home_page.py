from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SELENIUM_SERTIFICATION_PAGE_LINK = (By.XPATH, "//*[contains(@class, 'home-banner')]//a")
    
    ELEMENTS_BUTTON = (By.XPATH, "//div[contains(@class, 'card mt-4 top-card') and contains(., 'Elements')]")
    FORMS_BUTTON = (By.XPATH, "//div[contains(@class, 'card-body')]//*[contains(text(), 'Forms')]")
    ALERTS_FRAME_WINDOWS_BUTTON = (By.XPATH, "//div[contains(@class, 'card-body')]//*[contains(text(), 'Alerts, Frame & Windows')]")
    WIDGETS_BUTTON = (By.XPATH, "//div[contains(@class, 'card-body')]//*[contains(text(), 'Widgets')]")
    INTERACTIONS_BUTTON = (By.XPATH, "//div[contains(@class, 'card-body')]//*[contains(text(), 'Interactions')]")
    BOOK_STORE_BUTTON = (By.XPATH, "//div[contains(@class, 'card-body')]//*[contains(text(), 'Book Store')]")

    def click_on_certification_banner(self):
        self.find_element_clickable(*self.SELENIUM_SERTIFICATION_PAGE_LINK).click()

    def click_on_elements_button(self):
        element = self.find_element(*self.ELEMENTS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_forms_button(self):
        element = self.find_element(*self.FORMS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_alerts_frame_windows_button(self):
        element = self.find_element(*self.ALERTS_FRAME_WINDOWS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_widgets_button(self):
        element = self.find_element(*self.WIDGETS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_interactions_button(self):
        element = self.find_element(*self.INTERACTIONS_BUTTON)
        self.move_to_element(element)
        element.click()

    def click_on_book_store_button(self):
        element = self.find_element(*self.BOOK_STORE_BUTTON)
        self.move_to_element(element)
        element.click()
        