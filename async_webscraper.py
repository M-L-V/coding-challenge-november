import aiohttp
import asyncio
from bs4 import BeautifulSoup

#inspo https://understandingdata.com/posts/asynchronous-web-scraping-in-python/

class AsyncWebScraper(object):

    #create class
    def __init__(self, urls):
        self.urls = urls #set urls to be the urls passed in
        # Global Place To Store The Data:
        self.all_data  = []
        # Run The Scraper:
        asyncio.run(self.main())


    #fetch data
    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                text = await response.text()
                info_array = await self.extract_info(text) #run extracting required info function into an array
                return text, url, info_array
        except Exception as e:
            print(str(e))

    async def extract_info(self, text): 
        try:
            all_data = []
            soup = BeautifulSoup(text, 'html.parser')
            #handle parsing appropriately for property name, property type, number of bedrooms and bathrooms and list of amenities via soup
            #return as array of content, pushing into all_data and checking for errors at each stage
        except Exception as e:
            print(str(e))


    async def main(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls) #add to the all_data array

            # Storing the raw HTML data.
            for html in htmls:
                if html is not None:
                   print(html)
                else:
                    continue
