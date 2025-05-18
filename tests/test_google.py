import sys
import os


def test_google_title(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())
    assert "Google" in page.title()
