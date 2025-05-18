from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    print(type(browser))
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())
    browser.close()
