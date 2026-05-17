import pytest
from drivers.driver_setup import get_driver
from datetime import datetime

@pytest.fixture
def setup(request):
    driver = get_driver(headless=True)
    yield driver

    # Take screenshot if test fails
    if request.node.rep_call.failed:
        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        driver.save_screenshot(f"screenshots/{request.node.name}_{time}.png")

    driver.quit()

# Hook to know test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_maker_report(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)