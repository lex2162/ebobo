import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage

def test_successful_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url, "Не удалось авторизоваться"

def test_failed_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("wrong_user", "wrong_password")
    assert "Epic sadface" in page.get_error_message(), "Нет сообщения об ошибке"
