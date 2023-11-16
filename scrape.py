
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)



urls = [
    # 'https://www.airbnb.co.uk/rooms/33571268',
    'https://www.airbnb.co.uk/rooms/20669368',
    'https://www.airbnb.co.uk/rooms/50633275'
]



for url in urls:
    # navigate to airbnb on this specific url
    driver.get(url)

    # wait this length of time for the required element loads
    timeout = 30

    #set up expectations
    #expectations will EITHER return a selenium web element OR a boolean on successfully finding it

    #try to fetch title element
    try: 
        title_element_exists = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.hpipapi')), 'Title element not found within timeout') 

        if title_element_exists:
            print(title_element_exists.get_attribute('innerHTML'))
        else:
            print('cannot find title element')
    except Exception as e:
        print(e)


    #try to fetch type of house element
    try: 
        type_element_exists = WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'div.toieuka.dir.dir-ltr h1')), 'Type of house element not found within timeout')
        if type_element_exists:
                typeString = type_element_exists.get_attribute('innerHTML')
                print(typeString)
        else:
            print('cannot find house type element')
    except Exception as e:
        print(e)


    #try to fetch bathroom and bedroom elements
    # try:
    #     rooms = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.l7n4lsf.dir.dir-ltr'))
    #     allrooms = WebDriverWait(driver, timeout).until(rooms, message='Bedroom and bathroom element not found within timeout')

    #     for room in allrooms:
    #         #remove the bed number 
    #         # if room != driver.find_element("xpath",'//*[ substring(text(), string-length(text()) - string-length("bed") +1) = "bed"]'):
    #             print(room.get_attribute('innerHTML'), '//')

    # except Exception as e:
    #     print(e)


    #try to fetch amenties
    # try: 
    #     #find the amenities button by start and end of text of button and click it to create and launch the modal
    #     foundAmenitiesButton = WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.XPATH, '//*[starts-with(text(), "Show all") and substring(text(), string-length(text()) - string-length("amenities") +1) = "amenities"]')), 'Amenities button not found within timeout')
    #     foundAmenitiesButton.click()
    #     amenities_modal_found = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, '_17itzz4')), 'cannot find amenities modal')
    #     amenitytext = amenities_modal_found.get_attribute('innerHTML') #get the contents of the modal

    #     soup = BeautifulSoup(amenitytext, 'html.parser') #utilise Beautiful soup as HTML parser here
    #     amenitiesarray = soup.find_all('div', {"class": "twad414", "id": lambda x: x and x.startswith('pdp_v3')}) 

    #     if(amenitiesarray):
    #         for amenity in amenitiesarray:
    #             print(amenity.get_text())
    #     else:
    #         print('Cannot find amenities array')
    # except Exception as e: 
    #     print(e)
    
    print('-----')