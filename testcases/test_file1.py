from POM.playwrightpage import PlaywrightPage,expect


def test_get_started(setup):
    """
    Test navigation through the Playwright documentation website.

    Steps:
        1. Create a new browser context.
        2. Open a new browser page.
        3. Initialize the PlaywrightPage Page Object Model.
        4. Navigate to the Playwright homepage and verify the title.
        5. Click the Get Started button.
        6. Navigate to the Writing Tests section.
        7. Open the Test Assertions page.
        8. Verify the Assertions page title.

    Args:
        setup: Browser instance provided by the pytest fixture.
    """
    context = setup.new_context(no_viewport=True)

    page = context.new_page()

    pw = PlaywrightPage(page)

    pw.has_title()

    pw.get_started()

    expect(page).to_have_title("Assertions | Playwright")



