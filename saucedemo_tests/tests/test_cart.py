def test_add_item_to_cart(browser):
    """Тест добавления товара в корзину"""
    # Авторизация
    browser.login.open()
    browser.login.login("standard_user", "secret_sauce")

    # Добавляем товар в корзину
    browser.inventory.add_first_item_to_cart()
    assert browser.inventory.cart_item_count() == 1, "Товар не был добавлен в корзину"

    # Проверяем, что товар действительно в корзине
    browser.cart.open()
    assert browser.cart.get_cart_items() == 1, "Корзина не содержит добавленный товар"
