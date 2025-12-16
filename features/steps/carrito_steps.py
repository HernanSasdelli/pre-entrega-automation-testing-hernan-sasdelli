from behave import given, when, then
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given('estoy logueado como "{usuario}" con password "{password}"')
def step_impl(context, usuario, password):
    LoginPage(context.driver).abrir_pagina().login_completo(usuario, password)
    InventoryPage(context.driver).esperar_carga()

@when('agrego el producto "{nombre}" al carrito')
def step_impl(context, nombre):
    
    InventoryPage(context.driver).agregar_producto_por_id("add-to-cart-sauce-labs-backpack")

@when('abro el carrito')
def step_impl(context):
    InventoryPage(context.driver).ir_al_carrito()

@then('debo ver el producto "{nombre}" en el carrito')
def step_impl(context, nombre):
    cart = CartPage(context.driver).esperar_carga()
    assert nombre in cart.obtener_nombres_items()
