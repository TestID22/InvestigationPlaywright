import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def launch_browser(headless=False):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    return p, browser

