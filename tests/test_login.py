from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def test_login_exitoso(driver):
    driver.get(BASE_URL)

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    marca  = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".app_logo")))

    assert "inventory.html" in driver.current_url
    assert titulo.text.strip() == "Products"
    assert "Swag Labs" in marca.text