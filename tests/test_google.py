
def test_google_title(browser_page):
    browser_page.goto("https://www.google.com")
    print(browser_page.title())
    assert "Google" in browser_page.title(), "Title does not contain 'Google'"
