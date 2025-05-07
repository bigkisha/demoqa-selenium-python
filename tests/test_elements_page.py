import chromedriver_autoinstaller
import pytest

from selenium import webdriver
from pages.elements_page import ElementsPage

@pytest.fixture(scope="session")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def elements_page(driver):
    elements_page = ElementsPage(driver)
    elements_page.open("https://demoqa.com/elements")
    return elements_page

def test_click_on_text_box_button(driver, elements_page: ElementsPage):
    elements_page.click_on_text_box_button()
    
    assert "text-box" in driver.current_url, "Text Box page not opened."
    
    elements_page.back()

def test_click_on_check_box_button(driver, elements_page: ElementsPage):
    elements_page.click_on_check_box_button()
    
    assert "checkbox" in driver.current_url, "Check Box page not opened."
    
    elements_page.back()

def test_click_on_radio_button_button(driver, elements_page: ElementsPage):
    elements_page.click_on_radio_button_button()
    
    assert "radio-button" in driver.current_url, "Radio Button page not opened."
    
    elements_page.back()

def test_click_on_web_table_button(driver, elements_page: ElementsPage):
    elements_page.click_on_web_table_button()
    
    assert "webtables" in driver.current_url, "Web Tables page not opened."
    
    elements_page.back()

def test_click_on_buttons_button(driver, elements_page: ElementsPage):
    elements_page.click_on_buttons_button()
    
    assert "buttons" in driver.current_url, "Buttons page not opened."
    
    elements_page.back()

def test_click_on_links_button(driver, elements_page: ElementsPage):
    elements_page.click_on_links_button()
    
    assert "links" in driver.current_url, "Links page not opened."
    
    elements_page.back()

def test_click_on_broken_links_button(driver, elements_page: ElementsPage):
    elements_page.click_on_broken_links_button()
    
    assert "broken" in driver.current_url, "Broken Links - Images page not opened."
    
    elements_page.back()

def test_click_on_upload_and_download_button(driver, elements_page: ElementsPage):
    elements_page.click_on_upload_and_download_button()
    
    assert "upload-download" in driver.current_url, "Upload and Download page not opened."
    
    elements_page.back()

def test_click_on_dynamic_properties_button(driver, elements_page: ElementsPage):
    elements_page.click_on_dynamic_properties_button()
    
    assert "dynamic-properties" in driver.current_url, "Dynamic Properties page not opened."
    
    elements_page.back()