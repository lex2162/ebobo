from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Класс для работы со страницей товаров"""

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def open(self):
        self._open("https://www.saucedemo.com/")

    def add_first_item_to_cart(self):
        """Добавляет первый товар в корзину"""
        self._click_element(self.ADD_TO_CART_BUTTON)

    def cart_item_count(self):
        """Возвращает количество товаров в корзине"""
        cart_badge_text = self._get_text(self.CART_BADGE)
        try:
            return int(cart_badge_text)
        except ValueError:
            raise Exception(f"Произошло исключение. Локатор содержит {cart_badge_text}")
