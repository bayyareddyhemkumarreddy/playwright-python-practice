from POM.login_page import LoginPage
from playwright.sync_api import expect


def test_login(setup):
    """
    Verify that a registered user can log in successfully.

    Steps:
        1. Create a new browser context.
        2. Open a new browser page.
        3. Initialize the LoginPage POM class.
        4. Enter valid email and password.
        5. Click the Login button.
        6. Verify successful login.
        7. Close the browser context.

    Args:
        setup: Browser instance provided by pytest fixture.
    """

    context = setup.new_context(no_viewport=True)

    try:
        page = context.new_page()

        # Initialize Login Page Object
        p = LoginPage(page)

        # Enter login credentials
        p.login("hemreddy24@gmail.com", "H@e2mH@4")

        # Verify successful login
        expect(page).to_have_url(r"https://tutorialsninja.com/demo/index.php?route=account/account")

        expect(page.get_by_title("My Account", exact=True)).to_be_visible()

    finally:
        context.close()


