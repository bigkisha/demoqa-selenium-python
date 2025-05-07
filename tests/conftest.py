import pytest
import chromedriver_autoinstaller

from selenium import webdriver

@pytest.fixture(scope="session")
def driver():

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()