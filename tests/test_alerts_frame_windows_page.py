import chromedriver_autoinstaller
import pytest

from selenium import webdriver
from pages.alerts_frame_windows_page import AlertsFrameWindowsPage

@pytest.fixture
def alerts_frame_windows_page(driver):
    alerts_frame_windows_page = AlertsFrameWindowsPage(driver)
    alerts_frame_windows_page.open("https://demoqa.com/alerts")
    return alerts_frame_windows_page

def test_click_on_browsers_windows_button(driver, alerts_frame_windows_page: AlertsFrameWindowsPage):
    alerts_frame_windows_page.click_on_browsers_windows_button()
    
    assert "browser-windows" in driver.current_url, "Browser Windows page not opened."

def test_click_on_alerts_button(driver, alerts_frame_windows_page: AlertsFrameWindowsPage):
    alerts_frame_windows_page.click_on_alerts_button()
    
    assert "alerts" in driver.current_url, "Alerts page not opened."

def test_click_on_frames_button(driver, alerts_frame_windows_page: AlertsFrameWindowsPage):
    alerts_frame_windows_page.click_on_frames_button()
    
    assert "frames" in driver.current_url, "Frames page not opened."

def test_click_on_nested_frames_button(driver, alerts_frame_windows_page: AlertsFrameWindowsPage):
    alerts_frame_windows_page.click_on_nested_frames_button()
    
    assert "nestedframes" in driver.current_url, "Nested Frames page not opened."

def test_click_on_modal_dialogs_button(driver, alerts_frame_windows_page: AlertsFrameWindowsPage):
    alerts_frame_windows_page.click_on_modal_dialogs_button()
    
    assert "modal-dialogs" in driver.current_url, "Modal Dialogs page not opened."