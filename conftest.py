# conftest.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
SCREENS_DIR = os.path.join(REPORTS_DIR, "screens")

@pytest.fixture(scope="function")
def driver():
    os.makedirs(REPORTS_DIR, exist_ok=True)

    #SIEMPRE crear Options antes de usar opts.add_argument()
    opts = Options()

    #CI
    if os.getenv("GITHUB_ACTIONS") == "true":
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-gpu")

       #linx
        if os.name != "nt":
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")

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
def screenshot_on_failure(request):
    yield

    if "driver" not in request.fixturenames:
        return

    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        os.makedirs(SCREENS_DIR, exist_ok=True)

        ts = time.strftime("%Y%m%d-%H%M%S")
        safe = request.node.nodeid.replace("::", "-").replace("/", "_").replace("\\", "_")
        path = os.path.join(SCREENS_DIR, f"{safe}_FAIL_{ts}.png")

        try:
            drv = request.getfixturevalue("driver")
            drv.save_screenshot(path)
        except Exception:
            pass
