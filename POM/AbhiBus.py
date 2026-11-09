from playwright.sync_api import expect


class AbhiBus:
    """Page Object Model for booking bus tickets on the AbhiBus website."""

    def __init__(self, page):
        """Initialize the page object and define web elements."""
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

    def choose_bus_from_and_to_location(self, from_place, to_place):
        """
        Select the source and destination locations and search for buses.

        Args:
            from_place (str): Source or departure city.
            to_place (str): Destination city.

        Steps:
            1. Navigate to the AbhiBus website.
            2. Select the bus booking option.
            3. Enter the departure location.
            4. Enter the destination location.
            5. Click the search button.
        """
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

    def filter_boarding_point(self):
        """
        Filter available buses based on the selected boarding point.

        Steps:
            1. Wait for the search results to load.
            2. Open the boarding points filter.
            3. Select KPHB from the available boarding points.
        """
        self.page.wait_for_load_state()
        expect(self.boarding_point).to_be_visible()
        self.boarding_point.click()
        self.select_boarding_point.filter(has_text="kphb").first.click()

    def filter_dropping_point(self):
        """
        Filter available buses based on the selected dropping point.

        Steps:
            1. Open the dropping point filter.
            2. Select Majestic from the available dropping points.
        """
        expect(self.dropping_point).to_be_visible()
        self.dropping_point.click()
        self.select_boarding_point.filter(has_text="Majestic").first.click()

    def filter_operators(self):
        """
        Filter buses by operator and bus type.

        Steps:
            1. Open the operators filter.
            2. Select Prasanna - Purple operator.
            3. Open the bus type filter.
            4. Select the Sleeper checkbox.
            5. Verify that the Sleeper checkbox is selected.
        """
        self.operators.click()
        self.select_boarding_point.filter(has_text="Prasanna - Purple...").first.click()
        self.bus_type.click()
        expect(self.select_checkbox_sleeper).to_be_visible()
        self.select_checkbox_sleeper.nth(2).check()
        expect(self.select_checkbox_sleeper).to_be_checked(True)








