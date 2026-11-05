from playwright.sync_api import expect


class PlaywrightPage:

    def __init__(self, page):

        self.page = page
        self.url = "https://playwright.dev/"

        self.start_button = page.get_by_text("Get started", exact=True)

        self.writing_test = page.get_by_title("Writing tests")

        self.find_assert = page.get_by_role("heading", name="Assertions", exact=True)

    def has_title(self):

        self.page.goto(self.url)

        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    def get_started(self):

        self.page.goto(self.url)

        self.start_button.click()

        expect(self.page).to_have_title("Installation | Playwright")

        self.writing_test.click()

        expect(self.page).to_have_url(lambda url: "writing-tests" in url)

        expect(self.find_assert).to_be_visible()

        self.find_assert.click()