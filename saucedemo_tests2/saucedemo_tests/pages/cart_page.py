from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Класс для работы с корзиной"""

    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def get_cart_items(self):
        """Возвращает количество товаров в корзине"""
        return len(self.find_elements(*self.CART_ITEM))
