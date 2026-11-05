from POM.playwrightpage import PlaywrightPage,expect


def test_get_started(setup):
    context = setup.new_context(no_viewport=True)

    page = context.new_page()

    pw = PlaywrightPage(page)

    pw.has_title()

    pw.get_started()

    expect(page).to_have_title("Assertions | Playwright")



