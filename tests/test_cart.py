from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage


from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_carrito(driver):
    # 1) LOGIN
    LoginPage(driver).abrir_pagina().login_completo("standard_user", "secret_sauce")

    # AGREGAR Y ABRIR CARRITO
    inv = InventoryPage(driver).esperar_carga()
    inv.agregar_backpack_al_carrito()
    inv.ir_al_carrito()

   # WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    cart = CartPage(driver).esperar_carga()
    assert "cart.html" in driver.current_url

    # CARRITO
    cart = CartPage(driver).esperar_carga()
    assert "cart.html" in driver.current_url
    assert cart.hay_items() is True
    assert "Sauce Labs Backpack" in cart.obtener_nombres_items()
