PAGE_URL = "https://demoqa.com/nestedframes"


def test_demos_nested_iframe_exist(browser_page):
    browser_page.goto(PAGE_URL)
    main_frame = browser_page.main_frame
    sample_iframe = find_required_iframe_by_name_or_url(main_frame.child_frames, "frame1")
    nested_frames = sample_iframe.child_frames
    nested_frame = find_required_iframe_by_name_or_url(nested_frames, url="about:srcdoc")
    text_in_nested_frame = nested_frame.locator("//p").inner_text()
    assert text_in_nested_frame == "Child Iframe", "Text doesn't match"


def find_required_iframe_by_name_or_url(iframe_list: list, name: str | None = None, url: str | None = None):
    if name is not None and url is not None:
        raise ValueError("Cannot search by both")
    if name is None and url is None:
        raise ValueError("At least one param must be selected")

    try:
        if name is not None:
            for iframe in iframe_list:
                if iframe.name == name:
                    return iframe
        elif url is not None:
            # Search by url
            for iframe in iframe_list:
                if iframe.url == url:
                    return iframe
        return None
    except Exception as e:
        print(e)

