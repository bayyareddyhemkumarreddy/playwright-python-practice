#pre-requiste for Asynchronous execution
# install pytest-asyncio
from playwright.async_api import async_playwright,expect


async def test_verifyPageUrl():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.automationpractice.pl/index.php")  # passing url
        await expect(page).to_have_url("https://www.automationpractice.pl/index.php") #expected url
