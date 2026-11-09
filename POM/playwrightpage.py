from playwright.sync_api import expect


class PlaywrightPage:
    """Page Object Model for automating the Playwright documentation website."""
    def __init__(self, page):
        """
        Initialize the page object and define web elements.

        Args:
            page: Playwright Page instance.
        """
        self.page = page
        self.url = "https://playwright.dev/"
        self.start_button = page.get_by_text("Get started", exact=True)
        self.writing_test = page.get_by_title("Writing tests")
        self.find_assert = page.get_by_role("link", name="test assertions", exact=True)

    def has_title(self):
        """
        Navigate to the Playwright website and verify the page title.

        Steps:
            1. Open the Playwright website.
            2. Verify that the expected page title is displayed.
        """
        self.page.goto(self.url)

        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    def get_started(self):
        """
        Navigate through the Playwright documentation.

        Steps:
            1. Open the Playwright website.
            2. Click the Get started button.
            3. Verify the Installation page title.
            4. Navigate to the Writing tests section.
            5. Verify that the Test Assertions link is visible.
            6. Click the Test Assertions link.
        """

        self.page.goto(self.url)
        self.start_button.click()
        expect(self.page).to_have_title("Installation | Playwright")
        self.writing_test.click()
        expect(self.find_assert).to_be_visible()
        self.find_assert.click()