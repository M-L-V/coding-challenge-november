import asyncio

#trying to use async functions - https://quentin.pradet.me/blog/you-dont-need-promises-in-python-just-use-asyncawait.html

#https://understandingdata.com/posts/asynchronous-web-scraping-in-python/
#'Inside of your event loop, you can set a number of tasks to be completed and every task will be created and executed asychronously'

async def testing_async():
   print('testing async')

loop = asyncio.get_event_loop()
loop.run_until_complete(testing_async())
