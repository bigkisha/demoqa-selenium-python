from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AlertsFrameWindowsPage(BasePage):
    BROWSERS_WINDOWS_BUTTON = (By.XPATH, "//*[text()='Browser Windows']/ancestor::*[contains(@id, 'item-')]")
    ALERTS_BUTTON = (By.XPATH, "//*[text()='Alerts']/ancestor::*[contains(@id, 'item-')]")
    FRAME_BUTTON = (By.XPATH, "//*[text()='Frames']/ancestor::*[contains(@id, 'item-')]")
    MODAL_DIALOG_BUTTON = (By.XPATH, "//*[text()='Modal Dialogs']/ancestor::*[contains(@id, 'item-')]")
    NESTED_FRAMES_BUTTON = (By.XPATH, "//*[text()='Nested Frames']/ancestor::*[contains(@id, 'item-')]")
    NEW_WINDOW_BUTTON = (By.XPATH, "//*[text()='New Window']/ancestor::*[contains(@id, 'item-')]")

    def click_on_browsers_windows_button(self):
        element = self.find_element(*self.BROWSERS_WINDOWS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_alerts_button(self):
        element = self.find_element(*self.ALERTS_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_frames_button(self):
        element = self.find_element(*self.FRAME_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_nested_frames_button(self):
        element = self.find_element(*self.NESTED_FRAMES_BUTTON)
        self.move_to_element(element)
        element.click()
    
    def click_on_modal_dialogs_button(self):
        element = self.find_element(*self.MODAL_DIALOG_BUTTON)
        self.move_to_element(element)
        element.click()
    