import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def setup():
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=False,args=["--start-maximized"])
        yield browser
        browser.close()



