from POM.playwrightpage import PlaywrightPage,expect


def test_get_started(setup):

    page = setup.new_page()

    pw = PlaywrightPage(page)

    pw.has_title()

    pw.get_started()

    expect(page).to_have_title("Installation | Playwright")



