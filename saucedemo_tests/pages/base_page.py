from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _get_visibility_all_elements(self, locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def _get_visibility_element(self, locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def _get_clickable_element(self, locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def _open(self, link):
        self.driver.get(link)

    def _enter_text(self, locator, text, timeout=10):
        field = self._get_visibility_element(locator, timeout)
        field.clear()
        field.send_keys(text)

    def _click_element(self, locator, timeout=10):
        button = self._get_clickable_element(locator, timeout)
        button.click()

    def _get_text(self, locator, timeout=10):
        return self._get_visibility_element(locator, timeout).text
