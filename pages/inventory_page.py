from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Locators
    _TITLE = (By.CSS_SELECTOR, ".title")
    _APP_LOGO = (By.CSS_SELECTOR, ".app_logo")
    _CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    _CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # Producto 
    _ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_carga(self):
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return self

    def obtener_titulo(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return el.text

    def obtener_marca(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self._APP_LOGO))
        return el.text

    def agregar_backpack_al_carrito(self):
        btn = self.wait.until(EC.element_to_be_clickable(self._ADD_BACKPACK))
        btn.click()
        return self

    def obtener_cantidad_carrito(self) -> int:
        try:
            badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            return int(badge.text)
        except Exception:
            return 0

    def ir_al_carrito(self):
        link = self.wait.until(EC.element_to_be_clickable(self._CART_LINK))
        link.click()
        return self
    


    def agregar_producto_por_id(self, add_button_id: str):
        locator = (By.ID, add_button_id)
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()
        return self
    
    



