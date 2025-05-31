from playwright.sync_api import sync_playwright


# This function initializes a Playwright browser instance.
def web_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, args=['--start-maximized'],)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    return page, browser

