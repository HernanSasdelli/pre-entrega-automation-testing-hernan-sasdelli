from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # URL
    URL = "https://www.saucedemo.com/"

    # Locators
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_TEXT = (By.CSS_SELECTOR, ".error-message-container h3")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def completar_user(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_pass(self, password: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        campo.clear()
        campo.send_keys(password)
        return self

    def hacer_click_button(self):
        boton = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        boton.click()
        return self

    def login_completo(self, usuario: str, password: str):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self

    def obtener_error(self) -> str:
        div_error = self.wait.until(EC.visibility_of_element_located(self._ERROR_TEXT))
        return div_error.text
