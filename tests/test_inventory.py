from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def test_inventario_basico(driver):
    driver.get(BASE_URL)
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    assert titulo.text.strip() == "Products"

    # el primer producto visible
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item")))
    items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    assert len(items) >= 1

    # Nombre y precio
    nombre_primero = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")[0].text.strip()
    precio_primero = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")[0].text.strip()
    assert nombre_primero != ""
    assert precio_primero.startswith("$")

    # menu y filtros
    assert driver.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, ".product_sort_container").is_displayed()