from playwright.sync_api import sync_playwright

# This function initializes a Playwright browser instance.
def web_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return page, browser

