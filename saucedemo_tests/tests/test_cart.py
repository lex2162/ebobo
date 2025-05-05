def test_add_item_to_cart(driver, login_page, inventory_page, cart_page):
    """Тест добавления товара в корзину"""
    # Открываем страницу логина и логинимся
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товар в корзину
    inventory_page.add_first_item_to_cart()
    assert inventory_page.cart_item_count() == 1, "Товар не был добавлен в корзину"

    # Проверяем, что товар действительно в корзине
    cart_page.open()
    assert cart_page.get_cart_items() == 1, "Корзина не содержит добавленный товар"
