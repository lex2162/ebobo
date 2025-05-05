import pytest

def test_successful_login(login_page):
    """Тест успешного логина"""
    # Открываем страницу логина и выполняем вход
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Проверяем, что мы перешли на страницу инвентаря
    assert "inventory.html" in login_page.driver.current_url, "Не произошёл переход на страницу инвентаря"

def test_failed_login(login_page):
    """Тест неуспешного логина с некорректными данными"""
    # Открываем страницу логина и пытаемся войти с неверными данными
    login_page.open()
    login_page.login("invalid_user", "invalid_pass")

    # Проверяем, что выводится сообщение об ошибке
    error_text = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in error_text, f"Ожидали сообщение об ошибке, получили: {error_text}"
