import pytest
from selenium import webdriver
from utils.read_config import read_config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(scope="function")
def setup(request):
    browser = read_config("default", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(int(read_config("default", "implicit_wait")))
    driver.get(read_config("default", "base_url"))
    request.cls.driver = driver

    yield driver

    # Take screenshot if the test failed
    if request.node.rep_call.failed:
        screenshot_name = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_name)

    driver.quit()


# ✅ This hook sets test result info into request.node
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call (setup, call, teardown)
    setattr(item, "rep_" + rep.when, rep)
