
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

from tests import check_input_url

from selenium.webdriver.common.by import By


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox(options=options)



urls = [
    'https://www.airbnb.co.uk/rooms/33571268', #this is a 401 response
    'https://www.airbnb.co.uk/rooms/20669368',
    'https://www.airbnb.co.uk/rooms/50633275'
]



for url in urls:
    # navigate to airbnb on this specific url

    driver.get(url)

    # wait this length of time for the required element to load
    timeout = 30

    for request in driver.requests:
        if request.response: #currently pulling every request on the page
            print(
                request.host
            )
    
    
    print('-----')