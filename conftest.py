# conftest.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

@pytest.fixture(scope="function")
def driver():
    if not os.path.isdir(REPORTS_DIR):
        os.makedirs(REPORTS_DIR, exist_ok=True)
    opts = Options()
    drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(2)
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        ts = time.strftime("%Y%m%d-%H%M%S")
        safe = request.node.nodeid.replace("::", "-").replace("/", "_").replace("\\", "_")
        path = os.path.join(REPORTS_DIR, f"{safe}_FAIL_{ts}.png")
        try:
            driver.save_screenshot(path)
        except Exception:
            pass
