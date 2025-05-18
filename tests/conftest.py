import pytest
from framework.browser import launch_browser

@pytest.fixture
def browser():
    p, browser = launch_browser(headless=False)
    yield browser
    browser.close()
    p.stop()
