import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.datos import leer_csv_login


@pytest.mark.smoke
@pytest.mark.parametrize("usuario,password,espera_ok", leer_csv_login())
def test_login_desde_csv(driver, usuario, password, espera_ok):
    login = LoginPage(driver)
    login.abrir_pagina()
    login.login_completo(usuario, password)

    wait = WebDriverWait(driver, 10)

    if espera_ok:
        wait.until(EC.url_contains("/inventory.html"))
        assert "inventory.html" in driver.current_url
    else:
        assert "Epic sadface" in login.obtener_error()
