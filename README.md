# coding-challenge (and update November 2023 - see below)

**The project**

This was a practice of a coding challenge requiring you to scrape information from 3 provided Aibnb urls. The information required was 

- Property name
- Property type (e.g apartment)
- Number of bedrooms
- Number of bathrooms
- List of amenities

It was implemented in Python. 

**The stack chosen**

Airbnb's website is not a static website, and generates a lot of content with JavaScript. As such, it wasn't possible to use conventional basic web scraping (e.g, with Axios), so I utilised Selenium and its webdriver functionality (for Chrome) so I could control the browser and control accessing the elements when they loaded using Selenium's expected conditions to allow the webdriver to wait until the required elements had loaded.

I also used Beautiful Soup - an HTML parser for parsing what I received back, although I only did this in one instance as it didn't seem necessary for all.

**Running this coding challenge locally**

You will need to have Selenium installed on your machine. You can install it by running 
```pip install selenium```
If this doesn't work, try 
```pip3 install selenium```

If you get a ```Import "selenium" could not be resolved Pylance (reportMissingImports) error```, try 

```
1) Open the VS Command Pallette (for Windows use Ctrl+Shift+P)
2) Choose or type "Python: Select Interpreter"
3) Select your OS's default Python version (check your C: drive) or whichever Python version you installed Selenium to.
```
You will also need to install BeautifulSoup4 via 

```pip install beautifulsoup4```

**Challenges and next steps**

This project was an interesting challenge as I had not done Python before, but I felt it was the best language to do it in given the amount of documentation and StackOverflow queries covering webscraping in Python. I also had limited time due to doing this around my usual work. If given more time, I would do the following:

- Set up testing and more detailed error handling
- Better fetching of the elements - fetching by classname is unreliable as classnames can change, so I would spend more time looking into how to account for this (**Update November: This became evident as my scraping of the bathroom and bedroom content no longer worked as the markup had changed**)
- Turn this into a fullstack application - probably converting Python responses to JSON and creating an API a frontend application could consume
- Converting this into an OOP piece of code and utilising classes rather than just a list of functions
- Better git and version control - I just worked on the main branch and was not particularly detailed in commit messsages



**update November 2023**

**Specific feedback from June, and challenges faced in November** 

Challenges
- Unfortunately, due a hardware constraint, I only had an evening and part of a morning to try and iterate over my existing codebase from June. I discovered that a few functions no longer worked, either due to AirBnB's markup changing or the libraries updating their functionality due to version (e.g ```https://github.com/SeleniumHQ/selenium/blob/a4995e2c096239b42c373f26498a6c9bb4f2b3e7/py/CHANGES``` )

This has caused a significant challenge as my previous functions for fetching apartment type and others stopped working. I have left them in the code as examples of what I would have used if the web driver had been able to locate the elements. Given more time, I would debug each function to figure out why my previous approach of selecting them had stopped working. Alternatively, I would try a different approach such as the one in async_webscraper.py, which utilises aiohtto and asyncio. I also tried Playwright (```https://playwright.dev/```) as an alternative to Selenium, but found trying to learn a new library in a such a short time frame was too challenging and I didn't continue.


Feedback given when the challenge was first submitted in June 2023 is detailed below, as well as what I did to resolve it in November.

- Code should be split into functions

This has been done, although the functions do not return the required data.

- Better error handling

The main issue was how to handle urls that didn't return the expected webpage (e.g the url that returns a 401 response). I started looking into the requests property opf the web driver which retrieves the requests made between the browser and server, and would have worked on how to handle various responses to these, but ran out of time. Going forwards, I would learn how to effectively use this for error handling.

- Firefox and other browsers should have been included

I didn't have time to put this functionality into practice but am aware that Selenium webdriver offers Firefox and other browser functionality (```https://www.selenium.dev/documentation/webdriver/browsers/firefox/``) Going forwards, I would include this functionality.

- Stateless functions should be utilised where possible

Going forwards, I would learn more about stateless functions in Python as this is a knowledge gap currently. My understanding of this in the context of the current codebase is that I shouldn't be using if(element exists) then (do something) in the fetching functions, as this relies on the function having to keep a reference to these elements in state, which can lead to unexpected behaviour.

- Think about unit tests

I have provided an example of tests in general I would consider, such as checking the input url is a valid url. Going forwards, I would learn more about unit testing in Python as well as other validation requirements depending on the requirements of the application.

- Asynchronous programming

Unfortunately there was too much of a time constraint for me to put this feedback into practice with the existing codebase. I have given an example of a new approach I started in ```async_webscraper.py``` based off a tutorial (not using Webdriver); given more time I would explore this more and work on an async approach, as it is essential for web scraping given the time issues related to one request running at a single time.

- Docker for practicing running the app in different environments

Unfortunately I currently have too little knowledge of Docker currently for it to have been worth me trying to get this running in a Docker container within the time constraints. However, going forwards I would learn how to use Docker as it would be invaluable for testing and development purposes. I also considered using Python virtualenv for creating isolated Python environments to run the scraper in, but also ran into a time constraint and therefore in the future would also learn about this. 
