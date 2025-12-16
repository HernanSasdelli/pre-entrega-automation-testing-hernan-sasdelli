# conftest.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import configurar_logger

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
SCREENS_DIR = os.path.join(REPORTS_DIR, "screens")


LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
LOG_FILE = os.path.join(LOGS_DIR, "suite.log")


@pytest.fixture(scope="function")
def driver():
    # Carpetas
    if not os.path.isdir(REPORTS_DIR):
        os.makedirs(REPORTS_DIR, exist_ok=True)

    
    opts = Options()

    
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(2)
    yield drv
    drv.quit()

@pytest.fixture(scope="session", autouse=True)
def suite_logger():
    logger = configurar_logger(LOG_FILE)
    logger.info("=== INICIO SUITE ===")
    yield logger
    logger.info("=== FIN SUITE ===")

@pytest.fixture
def logger(suite_logger):
    return suite_logger



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed and "driver" in item.fixturenames:
        drv = item.funcargs.get("driver", None)
        if drv is None:
            return

        os.makedirs(SCREENS_DIR, exist_ok=True)

        #formatear fecha y hora standar como wp para evitar que se sobreescriba, si queremos que se sobreescriba sacar esta parte
        ts = time.strftime("%Y%m%d-%H%M%S")
        safe = item.nodeid.replace("::", "-").replace("/", "_").replace("\\", "_")
        path = os.path.join(SCREENS_DIR, f"{safe}_FAIL_{ts}.png")

        try:
            drv.save_screenshot(path)

            #Envia a carpeta /reports)
            rel_path = os.path.relpath(path, REPORTS_DIR)

            #pytest-html ->agrega la imagen
            try:
                import pytest_html
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(rel_path))
                rep.extra = extra
            except Exception:
                pass

        except Exception:
            pass
