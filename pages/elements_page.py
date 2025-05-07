from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    # Locators for the Elements page
    TEXT_BOX_BUTTON = (By.XPATH, "//*[text()='Text Box']/ancestor::*[contains(@id, 'item-')]")
    CHECK_BOX_BUTTON = (By.XPATH, "//*[text()='Check Box']/ancestor::*[contains(@id, 'item-')]")
    RADIO_BUTTON_BUTTON = (By.XPATH, "//*[text()='Radio Button']/ancestor::*[contains(@id, 'item-')]")
    WEB_TABLE_BUTTON = (By.XPATH, "//*[text()='Web Tables']/ancestor::*[contains(@id, 'item-')]")
    BUTTONS_BUTTON = (By.XPATH, "//*[text()='Buttons']/ancestor::*[contains(@id, 'item-')]")
    LINKS_BUTTON = (By.XPATH, "//*[text()='Links']/ancestor::*[contains(@id, 'item-')]")
    BROKEN_LINKS_BUTTON = (By.XPATH, "//*[text()='Broken Links - Images']/ancestor::*[contains(@id, 'item-')]")
    UPLOAD_AND_DOWNLOAD_BUTTON = (By.XPATH, "//*[text()='Upload and Download']/ancestor::*[contains(@id, 'item-')]")
    DYNAMIC_PROPERTIES_BUTTON = (By.XPATH, "//*[text()='Dynamic Properties']/ancestor::*[contains(@id, 'item-')]")

    def click_on_text_box_button(self):
        element = self.find_element(*self.TEXT_BOX_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_check_box_button(self):
        element = self.find_element(*self.CHECK_BOX_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_radio_button_button(self):
        element = self.find_element(*self.RADIO_BUTTON_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_web_table_button(self):
        element = self.find_element(*self.WEB_TABLE_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_buttons_button(self):
        element = self.find_element(*self.BUTTONS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_links_button(self):
        element = self.find_element(*self.LINKS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_broken_links_button(self):
        element = self.find_element(*self.BROKEN_LINKS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_upload_and_download_button(self):
        element = self.find_element(*self.UPLOAD_AND_DOWNLOAD_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_dynamic_properties_button(self):
        element = self.find_element(*self.DYNAMIC_PROPERTIES_BUTTON)
        self.move_to_element(element)
        element.click()