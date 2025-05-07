import chromedriver_autoinstaller
import pytest

from selenium import webdriver
from pages.widgets_page import WidgetsPage

@pytest.fixture(scope="session")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def widgets_page(driver):
    widgets_page = WidgetsPage(driver)
    widgets_page.open("https://demoqa.com/widgets")
    return widgets_page

def test_click_on_accordian_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_accordian_button()
    
    assert "accordian" in driver.current_url, "Accordian page not opened."

def test_click_on_auto_complete_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_auto_complete_button()
    
    assert "auto-complete" in driver.current_url, "Auto Complete page not opened."

def test_click_on_date_picker_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_date_picker_button()
    
    assert "date-picker" in driver.current_url, "Date Picker page not opened."

def test_click_on_slider_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_slider_button()
    
    assert "slider" in driver.current_url, "Slider page not opened."

def test_click_on_progress_bar_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_progress_bar_button()
    
    assert "progress-bar" in driver.current_url, "Progress Bar page not opened."

def test_click_on_tabs_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_tabs_button()
    
    assert "tabs" in driver.current_url, "Tabs page not opened."

def test_click_on_tool_tips_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_tool_tips_button()
    
    assert "tool-tips" in driver.current_url, "Tool Tips page not opened."

def test_click_on_menu_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_menu_button()
    
    assert "menu" in driver.current_url, "Menu page not opened."

def test_click_on_select_menu_button(driver, widgets_page: WidgetsPage):
    widgets_page.click_select_menu_button()
    
    assert "select-menu" in driver.current_url, "Select Menu page not opened."