from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WidgetsPage(BasePage):
    ACCORDIAN_BUTTON = (By.XPATH, "//*[text()='Accordian']/ancestor::*[contains(@id, 'item-')]")
    AUTO_COMPLETE_BUTTON = (By.XPATH, "//*[text()='Auto Complete']/ancestor::*[contains(@id, 'item-')]")
    DATE_PICKER_BUTTON = (By.XPATH, "//*[text()='Date Picker']/ancestor::*[contains(@id, 'item-')]")
    SLIDER_BUTTON = (By.XPATH, "//*[text()='Slider']/ancestor::*[contains(@id, 'item-')]")
    PROGRESS_BAR_BUTTON = (By.XPATH, "//*[text()='Progress Bar']/ancestor::*[contains(@id, 'item-')]")
    TABS_BUTTON = (By.XPATH, "//*[text()='Tabs']/ancestor::*[contains(@id, 'item-')]")
    TOOL_TIPS_BUTTON = (By.XPATH, "//*[text()='Tool Tips']/ancestor::*[contains(@id, 'item-')]")
    MENU_BUTTON = (By.XPATH, "//*[text()='Menu']/ancestor::*[contains(@id, 'item-')]")
    SELECT_MENU_BUTTON = (By.XPATH, "//*[text()='Select Menu']/ancestor::*[contains(@id, 'item-')]")

    def click_accordian_button(self):
        element = self.find_element(*self.ACCORDIAN_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_auto_complete_button(self):
        element = self.find_element(*self.AUTO_COMPLETE_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_date_picker_button(self):
        element = self.find_element(*self.DATE_PICKER_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_slider_button(self):
        element = self.find_element(*self.SLIDER_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_progress_bar_button(self):
        element = self.find_element(*self.PROGRESS_BAR_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_tabs_button(self):
        element = self.find_element(*self.TABS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_tool_tips_button(self):
        element = self.find_element(*self.TOOL_TIPS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_menu_button(self):
        element = self.find_element(*self.MENU_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_select_menu_button(self):
        element = self.find_element(*self.SELECT_MENU_BUTTON)
        self.move_to_element(element)
        element.click()