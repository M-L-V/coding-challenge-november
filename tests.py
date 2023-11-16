
#https://snyk.io/blog/secure-python-url-validation/

import validators
import unittest

#check inputted AirBNB url is a valid url
def check_input_url(input): 
    validation = validators.url(input)
    if validation:
        print('url is valid')
    else:
        print('not a valid url')

#Other test ideas
#check received data is string type
#check HTTP response of page