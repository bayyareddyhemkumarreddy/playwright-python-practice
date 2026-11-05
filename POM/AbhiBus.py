from playwright.sync_api import expect


class AbhiBus:

    def __init__(self, page):
        self.page = page

        self.url = "https://www.abhibus.com/"

        self.select_buses = page.locator("#bus-link")
        self.fm = page.get_by_placeholder("Leaving From")
        self.to = page.get_by_placeholder("Going To")
        self.search = page.locator("div#search-button").first
        self.boarding_point=page.get_by_text("Boarding Points").first
        self.select_boarding_point=page.locator("#popular-filters-scrollable")
        self.dropping_point=page.locator("btn  light outlined primary sm rounded-sm active button").first
        self.operators=page.get_by_text("Operators")
        self.bus_type=page.get_by_text("Bus Type")
        self.select_checkbox_sleeper=page.get_by_role("checkbox",name="Sleeper")

    def book_buses(self, from_place, to_place):
        self.page.goto(self.url)

        self.page.wait_for_load_state()

        expect(self.select_buses).to_be_visible()
        self.select_buses.click()

        expect(self.fm).to_be_visible()
        self.fm.click()
        self.fm.fill(from_place)
        self.fm.press("Enter")

        expect(self.to).to_be_visible()
        self.to.click()
        self.to.fill(to_place)
        self.to.press("Enter")

        expect(self.search).to_be_visible()
        expect(self.search).to_be_enabled()

        self.search.click()

        self.page.wait_for_load_state()
        expect(self.boarding_point).to_be_visible()
        self.boarding_point.click()
        self.select_boarding_point.filter(has_text="kphb").first.click()
        expect(self.dropping_point).to_be_visible()
        self.dropping_point.click()
        self.select_boarding_point.filter(has_text="Majestic").first.click()
        self.operators.click()
        self.select_boarding_point.filter(has_text="Prasanna - Purple...").first.click()
        self.bus_type.click()
        expect(self.select_checkbox_sleeper).to_be_visible()
        self.select_checkbox_sleeper.nth(2).check()
        expect(self.select_checkbox_sleeper).to_be_checked(True)








