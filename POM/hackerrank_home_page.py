class HackerRankHomePage:
    def __init__(self, page):
        self.page = page
        self.url="https://www.hackerrank.com/"
        self.scroll_to_element_start=self.page.get_by_text("Ready to hire for the ")
        self.click_play_button=self.page.get_by_role("button",name="Watch the DeepL story")
        self.close=self.page.get_by_role("button",name="Close video")
        self.products=self.page.locator('//summary[text()="Products"]')

    def get_home_page_title(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state()
        return self.page

    def scroll_to_element(self):
        self.scroll_to_element_start.scroll_into_view_if_needed()

    def play_video(self):
        self.click_play_button.click()

    def close_video(self):
        self.close.click()

    def select_product(self):
        self.products.is_visible()
        self.products.locator('//a[text()="Chakra"]').nth(0).click()


