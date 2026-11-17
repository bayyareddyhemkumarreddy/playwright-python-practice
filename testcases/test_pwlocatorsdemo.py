import re

from playwright.sync_api import Page, expect

#get_by_alt_text() locate img,logo,product images
#get_by_text() to locate visible text
#get_by_role() to locate using role
#get_by_label() representing beside element
#get_by_placeholder() it is attribute
#get_by_title() we can use if element has title attribute
#get_by_test_id() we use attribute value of data-test-id

def test_verify_pwlocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    logo=page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    text=page.get_by_text("Welcome to our store")# full text
    expect(text).to_be_visible()
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()# reg exp

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    expect(page.get_by_role("heading",name="Register")).to_be_visible()

    page.get_by_label("First name:").fill("hem reddy")
    page.get_by_label("Male").check()

    page.get_by_placeholder("Search store").fill("laptop")

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    t=page.get_by_title("Home Page Link")
    expect(t).to_have_text("Home")

    id=page.get_by_test_id("profile-name")
    expect(id).to_have_text("John Doe")