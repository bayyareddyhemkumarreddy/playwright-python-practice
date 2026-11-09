from POM.AbhiBus import AbhiBus

def test_select_bus(setup):
    """
    Test bus search functionality and apply different filters on AbhiBus.

    Steps:
        1. Create a new browser context.
        2. Open a new browser page.
        3. Initialize the AbhiBus Page Object Model.
        4. Select Bengaluru as the departure location.
        5. Select Hyderabad as the destination.
        6. Apply KPHB boarding point filter.
        7. Apply Majestic dropping point filter.
        8. Filter buses by operator and Sleeper bus type.
        9. Close the browser context after test execution.

    Args:
        setup: Browser instance provided by the pytest fixture.
    """
    context = setup.new_context(no_viewport=True)

    try:
        page = context.new_page()
        abhi_bus = AbhiBus(page)
        abhi_bus.choose_bus_from_and_to_location("Bengaluru","Hyderabad")
        abhi_bus.filter_boarding_point()
        abhi_bus.filter_dropping_point()
        abhi_bus.filter_operators()
    finally:
        context.close()