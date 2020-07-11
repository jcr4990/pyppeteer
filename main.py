import time
import asyncio
from pyppeteer.launcher import launch

URL = "https://www.gideonsgallery.com/shop-all"
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(URL, {'waitUntil': 'networkidle2'})

    while True:
        loadbtn = await page.querySelector("[data-hook='load-more-button']")

        try:
            loadbtntext = await loadbtn.getProperty('textContent')
        except AttributeError:
            break
        
        
        await loadbtn.click()
        loadbtn = None
        await asyncio.sleep(1)


    elements = await page.querySelectorAll("[data-hook='product-item-name']")
    await elements[-1].hover()
    await asyncio.sleep(2)
    await page.screenshot({'path': 'test.png'})
    

    #

    # elements = await page.querySelectorAll("[data-hook='product-item-name']")

    # for element in elements:
    #     element = await element.getProperty('textContent')
    #     element = await element.jsonValue()
    #     print(element)



asyncio.get_event_loop().run_until_complete(main())