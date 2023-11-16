
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

from tests import check_input_url
from functions import fetch_title, fetch_house_type, fetch_amenities, fetch_bathrooms_bedrooms

from selenium.webdriver.common.by import By


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)


urls = [
    'https://www.airbnb.co.uk/rooms/33571268', 
    'https://www.airbnb.co.uk/rooms/20669368',
    'https://www.airbnb.co.uk/rooms/50633275'
]



for url in urls:
    timeout = 30

    # navigate to airbnb on this specific url
    driver.get(url)

    # wait this length of time for the required element to load
    timeout = 30

   # try to fetch title element
    # fetch_title(timeout)
    
   # try to fetch type of house element
    # fetch_house_type(url, timeout)

   # try to fetch bathroom and bedroom elements
    # fetch_bathrooms_bedrooms(url, timeout)


    #try to fetch amenties
    # fetch_amenities(url, timeout)

    
    print('-----')