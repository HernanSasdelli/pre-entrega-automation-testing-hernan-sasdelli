from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def test_carrito_agrega_primer_producto(driver):
    driver.get(BASE_URL)
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))

    # Agrego el primer pprducto
    add_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[id^='add-to-cart-']")))
    add_buttons[0].click()

    # Badge = 1
    badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    assert badge.text.strip() == "1"

    # Entrar al carrito y verificar el item agregado
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    item_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name")))
    item_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
    assert item_name.text.strip() != ""
    assert item_price.text.strip().startswith("$")