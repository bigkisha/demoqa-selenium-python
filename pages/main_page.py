from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    SELENIUM_SERTIFICATION_PAGE_LINK = (By.XPATH, "//*[contains(@class, 'home-banner')]//a")

    def click_on_certification_banner(self):
        self.find_element_clickable(*self.SELENIUM_SERTIFICATION_PAGE_LINK).click()
        self.switch_to_next_tab()