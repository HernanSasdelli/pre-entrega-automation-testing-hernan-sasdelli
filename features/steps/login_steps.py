from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

@given('estoy en la pagina de login')
def step_impl(context):
    LoginPage(context.driver).abrir_pagina()

@when('ingreso usuario "{usuario}" y password "{password}"')
def step_impl(context, usuario, password):
    LoginPage(context.driver).login_completo(usuario, password)

@then('debo ver la pagina de productos')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("/inventory.html"))
    assert "inventory.html" in context.driver.current_url
