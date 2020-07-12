import asyncio
from pyppeteer.launcher import launch

URL = "https://www.gideonsgallery.com/shop-all"
prices = []


async def main():
    browser = await launch()  # headless=False
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(URL, {'waitUntil': 'networkidle2'})

    while True:
        loadbtn = await page.querySelector("[data-hook='load-more-button']")

        if loadbtn == None:
            break

        await loadbtn.click()
        await asyncio.sleep(1)

    elements = await page.querySelectorAll("[data-hook='product-item-name']")
    await elements[-1].hover()
    await asyncio.sleep(2)
    await page.screenshot({'path': 'test.png'})

    await asyncio.sleep(2)
    price_elems = await page.querySelectorAll("[data-hook='product-item-price-to-pay']")
    for element in price_elems:
        try:
            element = await element.getProperty('innerText')
            element = await element.jsonValue()
            price = element.replace("$", "").replace(
                ".00", "").replace(",", "")
            prices.append(price)
        except AttributeError:
            pass

    for i in prices:
        print(i)

    # PRINT TITLES
    # elements = await page.querySelectorAll("[data-hook='product-item-name']")

    # for element in elements:
    #     element = await element.getProperty('textContent')
    #     element = await element.jsonValue()
    #     print(element)


asyncio.get_event_loop().run_until_complete(main())
