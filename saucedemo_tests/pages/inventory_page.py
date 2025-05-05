from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Класс для работы со страницей инвентаря"""

    FIRST_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_ITEM_COUNT = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def add_first_item_to_cart(self):
        """Добавляет первый товар в корзину"""
        self._click_element(self.FIRST_ITEM_ADD_BUTTON)

    def cart_item_count(self):
        """Возвращает количество товаров в значке корзины"""
        text = self._get_text(self.CART_ITEM_COUNT)
        return int(text) if text else 0
