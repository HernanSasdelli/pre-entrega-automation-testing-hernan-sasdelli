from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    #print(">>> before_scenario OK")
    #...
    opts = Options()
    context.driver = webdriver.Chrome(options=opts)
    context.driver.implicitly_wait(2)


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
