from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Класс для работы со страницей товаров"""

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item_to_cart(self):
        """Добавляет первый товар в корзину"""
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def cart_item_count(self):
        """Возвращает количество товаров в корзине"""
        try:
            return int(self.find_element(*self.CART_BADGE).text)
        except:
            return 0
        # 123
        def
