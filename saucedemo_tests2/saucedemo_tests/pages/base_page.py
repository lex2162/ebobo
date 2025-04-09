from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_text(self, by, locator, text):
        field = self.wait.until(EC.visibility_of_element_located((by, locator)))
        field.clear()
        field.send_keys(text)

    def click_element(self, by, locator):
        button = self.wait.until(EC.element_to_be_clickable((by, locator)))
        button.click()

    def get_text(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text
