from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir_pagina()
    login.login_completo("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    marca = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".app_logo")))

    assert "inventory.html" in driver.current_url
    assert titulo.text.strip() == "Products"
    assert "Swag Labs" in marca.text

def test_login_exitoso(driver, logger):
    logger.info("UI - Inicio test_login_exitoso")
    ...
