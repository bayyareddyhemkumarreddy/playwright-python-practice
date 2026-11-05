from playwright.sync_api import expect


class AbhiBus:

    def __init__(self, page):
        self.page = page

        self.url = "https://www.abhibus.com/"

        self.select_buses = page.locator("#bus-link")
        self.fm = page.get_by_placeholder("Leaving From")
        self.to = page.get_by_placeholder("Going To")
        self.search = page.get_by_text(
            "Search Buses", exact=True
        )

    def book_buses(self, from_place, to_place):

        self.page.goto(self.url)

        expect(self.select_buses).to_be_visible()
        self.select_buses.click()

        expect(self.fm).to_be_visible()
        self.fm.fill(from_place)

        expect(self.to).to_be_visible()
        self.to.fill(to_place)

        expect(self.search).to_be_visible()
        expect(self.search).to_be_enabled()

        self.search.click()