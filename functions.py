
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


def fetch_title(timeout):
    try: 
        title_element_exists = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.hpipapi.i1pmzyw7.dir.dir-ltr')), 'Title element not found within timeout') 
        print(title_element_exists.get_attribute('innerHTML'))

    except Exception as e:
        print(e)


def fetch_house_type(timeout):
#try to fetch type of house element
    try: 
        type_element_exists = WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'div.toieuka.dir.dir-ltr h1')), 'Type of house element not found within timeout')
        if type_element_exists:
                typeString = type_element_exists.get_attribute('innerHTML')

                #trim the string by removing the host name
                split = typeString.split()

                remove_from = 'hosted'
                target_index = split.index(remove_from)
                trimmedarray = split[:target_index]

                typestring = ' '.join(trimmedarray)
                print(typestring)
        else:
            print('cannot find house type element')
    except Exception as e:
        print(e)


def fetch_bathrooms_bedrooms(timeout):
    #try to fetch bathroom and bedroom elements
    try:
        rooms = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.pen26si.dir.dir-ltr + span'))
        allrooms = WebDriverWait(driver, timeout).until(rooms, message='Bedroom and bathroom element not found within timeout')

        for room in allrooms:
            #remove the bed number 
            if room != driver.find_element_by_xpath('//*[ substring(text(), string-length(text()) - string-length("bed") +1) = "bed"]'):
                print(room.get_attribute('innerHTML'))
    except Exception as e:
        print(e)


def fetch_amenities(timeout):
    #try to fetch amenties
    try: 
        #find the amenities button by start and end of text of button and click it to create and launch the modal
        foundAmenitiesButton = WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.XPATH, '//*[starts-with(text(), "Show all") and substring(text(), string-length(text()) - string-length("amenities") +1) = "amenities"]')), 'Amenities button not found within timeout')
        foundAmenitiesButton.click()
        amenities_modal_found = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, '_17itzz4')), 'cannot find amenities modal')
        amenitytext = amenities_modal_found.get_attribute('innerHTML') #get the contents of the modal

        soup = BeautifulSoup(amenitytext, 'html.parser') #utilise Beautiful soup as HTML parser here
        amenitiesarray = soup.find_all('div', {"class": "twad414", "id": lambda x: x and x.startswith('pdp_v3')}) 

        if(amenitiesarray):
            for amenity in amenitiesarray:
                print(amenity.get_text())
        else:
            print('Cannot find amenities array')
    except Exception as e: 
        print(e)
