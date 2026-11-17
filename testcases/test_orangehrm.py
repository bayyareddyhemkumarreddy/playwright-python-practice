from playwright.sync_api import Page,expect

def test_orangehrm(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    expect(page).to_have_title("OrangeHRM")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    print(page.get_by_placeholder("Password").input_value())
    page.locator('//button[@type="submit"]').click()

    expect(page.get_by_role("heading",name="Dashboard")).to_have_text("Dashboard")
    page.locator('//span[text()="Admin"]').click()
    expect(page.get_by_role("heading",name="Admin")).to_have_text("Admin")
    page.get_by_text("Job").first.click()
    page.locator('//a[text()="Work Shifts"]').click()
    expect(page.get_by_role("heading",name="Work Shifts")).to_have_text("Work Shifts")
    checkboxs = page.locator('//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]')
    checkboxs.nth(2).check()
    page.locator('//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
    expect(page.get_by_role("heading",name="Add Work Shift")).to_have_text("Add Work Shift")
    page.locator('//input[@class="oxd-input oxd-input--active"]').nth(1).fill("Morning Shift")
    page.get_by_placeholder("hh:mm").nth(0).fill("07:00 AM")
    page.get_by_placeholder("hh:mm").nth(1).fill("03:00 PM")
    page.get_by_placeholder("Type for hints...").fill("John Carter")
    page.locator('//button[@type="submit"]').click()

