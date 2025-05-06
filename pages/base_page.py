from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))
    
    def find_element_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))
    
    def switch_to_next_tab(self):
        handles = self.driver.window_handles
        current = self.driver.current_window_handle
        current_index = handles.index(current)
        next_index = (current_index + 1) % len(handles)
        self.driver.switch_to.window(handles[next_index])
    
    def switch_to_previous_tab(self):
        handles = self.driver.window_handles
        current = self.driver.current_window_handle
        current_index = handles.index(current)
        previous_index = (current_index - 1) % len(handles)
        self.driver.switch_to.window(handles[previous_index])

    def open(self, url):
        self.driver.get(url)