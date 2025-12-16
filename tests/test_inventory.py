from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_catalogo(driver):
    # 1) Login
    LoginPage(driver).abrir_pagina().login_completo("standard_user", "secret_sauce")

    # 2) Inventario
    inv = InventoryPage(driver)
    inv.esperar_carga()

    # Si querés mantener el wait de URL como en tu test anterior:
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    assert "inventory.html" in driver.current_url
    assert inv.obtener_titulo().strip() == "Products"
    assert "Swag Labs" in inv.obtener_marca()
