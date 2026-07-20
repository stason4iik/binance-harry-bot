from playwright.async_api import async_playwright
from config import BINANCE_PROFILE


async def get_latest_post():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            BINANCE_PROFILE,
            wait_until="networkidle"
        )

        await page.wait_for_timeout(5000)

        text = await page.locator(
            "body"
        ).inner_text()

        await browser.close()

        return text