

def test_demos_nested_iframe_exist(browser_page):
    browser_page.goto("https://demoqa.com/nestedframes")
    assert browser_page.get_by_text("Nested")
    main_frame = browser_page.frame_locator("frame1")
    print(main_frame.child_frames())
