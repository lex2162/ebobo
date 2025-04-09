import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(browser):
    """Тест добавления товара в корзину"""

    # Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товар в корзину
    inventory_page = InventoryPage(browser)
    inventory_page.add_first_item_to_cart()
    assert inventory_page.cart_item_count() == 1, "Товар не был добавлен в корзину"

    # Проверяем, что товар действительно в корзине
    cart_page = CartPage(browser)
    cart_page.open("https://www.saucedemo.com/cart.html")
    assert cart_page.get_cart_items() == 1, "Корзина не содержит добавленный товар"
