import chromedriver_autoinstaller

from selenium import webdriver
from pages.main_page import MainPage

import pytest

@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_click_on_certification_banner(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com/")
    
    main_page.click_on_certification_banner()
    
    # Verify that the URL has changed to the certification page
    assert "selenium-training" in driver.current_url, "Certification page not opened."