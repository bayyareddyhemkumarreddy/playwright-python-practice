#simple testcase
from playwright.sync_api import Page,expect

def test_verifyPageUrl(page: Page):
    page.goto("https://www.automationpractice.pl/index.php") #passing url
    myurl=page.url
    print("url of the application:",myurl)
    expect(page).to_have_url("https://www.automationpractice.pl/index.php") #expected url

def test_verifyTitle(page: Page):
    page.goto("https://www.automationpractice.pl/index.php")
    page.wait_for_load_state()
    mytitle=page.title()
    print("title of the application:",mytitle)
    expect(page).to_have_title("My Shop")

