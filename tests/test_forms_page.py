import chromedriver_autoinstaller

from selenium import webdriver
from pages.forms_page import FormsPage

import pytest

@pytest.fixture(scope="session")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def forms_page(driver):
    forms_page = FormsPage(driver)
    forms_page.open("https://demoqa.com/forms")
    return forms_page

def test_click_on_practice_form_button(driver, forms_page: FormsPage):
    forms_page.click_practice_form_button()
    
    assert "practice-form" in driver.current_url, "Practice Form page not opened."