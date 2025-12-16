import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.datos import leer_json_productos


@pytest.mark.parametrize("nombre_producto,add_button_id", leer_json_productos())
def test_carrito_desde_json(driver, nombre_producto, add_button_id):
    #LOGIN
    LoginPage(driver).abrir_pagina().login_completo("standard_user", "secret_sauce")

    #AGREGAR PRODUCTO
    inv = InventoryPage(driver).esperar_carga()
    inv.agregar_producto_por_id(add_button_id)
    inv.ir_al_carrito()

    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    #VALIDAR
    cart = CartPage(driver).esperar_carga()
    nombres = cart.obtener_nombres_items()

    assert nombre_producto in nombres
