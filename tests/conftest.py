import pytest
from framework.web_browser import web_browser


@pytest.fixture
def browser_page():
    p, web_browser_instance = web_browser()
    yield p
    p.close()
    web_browser_instance.close()
