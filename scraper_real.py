import asyncio
import pytesseract
from PIL import Image
from playwright.async_api import async_playwright

async def scrape_last_multipliers():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.premierbet.com/tg/casino/game/aviator-2007", timeout=60000)
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshot.png", full_page=True)
        await browser.close()
    image = Image.open("screenshot.png")
    text = pytesseract.image_to_string(image)
    import re
    matches = re.findall(r'x?\s?(\d+\.\d+)', text)
    return [float(m) for m in matches if float(m) <= 100.0]
