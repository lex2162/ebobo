from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """Класс для работы с корзиной"""

    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def open(self):
        """Открывает страницу корзины"""
        self._open("https://www.saucedemo.com/cart.html")

    def get_cart_items(self):
        """Возвращает количество товаров в корзине"""
        cart_items = self._get_visibility_all_elements(self.CART_ITEM, timeout=5)
        return len(cart_items)
