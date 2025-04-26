from selenium import webdriver
from .cart_page import CartPage
from .inventory_page import InventoryPage
from .login_page import LoginPage

class ChromeDriver:
    def __init__(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver

    @property
    def cart(self):
        return CartPage(self.driver)

    @property
    def inventory(self):
        return InventoryPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)
