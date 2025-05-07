import chromedriver_autoinstaller
import pytest

from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    home_page.open("https://demoqa.com/")
    return home_page

def test_click_on_certification_banner(driver, home_page: HomePage):
    home_page.click_on_certification_banner()
    
    home_page.switch_to_next_tab()

    assert "selenium-training" in driver.current_url, "Certification page not opened."

    home_page.switch_to_previous_tab()

def test_click_on_elements_button(driver, home_page: HomePage):
    home_page.click_on_elements_button()
    
    assert "elements" in driver.current_url, "Elements page not opened."

    home_page.back()

def test_click_on_forms_button(driver, home_page: HomePage):
    home_page.click_on_forms_button()
    
    assert "forms" in driver.current_url, "Forms page not opened."

    home_page.back()

def test_click_on_alerts_frame_windows_button(driver, home_page: HomePage):
    home_page.click_on_alerts_frame_windows_button()
    
    assert "alertsWindows" in driver.current_url, "Alerts, Frame & Windows page not opened."

    home_page.back()

def test_click_on_widgets_button(driver, home_page: HomePage):
    home_page.click_on_widgets_button()
    
    assert "widgets" in driver.current_url, "Widgets page not opened."

    home_page.back()
    
def test_click_on_interactions_button(driver, home_page: HomePage):
    home_page.click_on_interactions_button()
    
    assert "interaction" in driver.current_url, "Interactions page not opened."

    home_page.back()

def test_click_on_book_store_button(driver, home_page: HomePage):
    home_page.click_on_book_store_button()
    
    assert "books" in driver.current_url, "Book Store page not opened."

    home_page.back()