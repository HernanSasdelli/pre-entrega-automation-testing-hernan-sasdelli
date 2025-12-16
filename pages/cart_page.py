from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Locators
    _TITLE = (By.CSS_SELECTOR, ".title")
    _CART_ITEM = (By.CSS_SELECTOR, ".cart_item")
    _ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_carga(self):
        self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return self

    def hay_items(self) -> bool:
        items = self.driver.find_elements(*self._CART_ITEM)
        return len(items) > 0

    def obtener_nombres_items(self):
        self.wait.until(EC.presence_of_all_elements_located(self._ITEM_NAME))
        elementos = self.driver.find_elements(*self._ITEM_NAME)
        return [e.text.strip() for e in elementos]
