from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")

    def open(self):
        self._open("https://www.saucedemo.com/")

    def login(self, username, password):
        self._enter_text(self.USERNAME_FIELD, username)
        self._enter_text(self.PASSWORD_FIELD, password)
        self._click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self._get_text(self.ERROR_MESSAGE)
