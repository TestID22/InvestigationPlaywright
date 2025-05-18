
def test_google_title(browser):
    browser.goto("https://www.google.com")
    print(browser.title())
    assert "Google" in browser.title(), "Title does not contain 'Google'"
