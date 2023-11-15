#assert that input is a URL
#assert that webdriver can connect
#assert type of whatever is being returned
#https://snyk.io/blog/secure-python-url-validation/

import validators

def check_input_url(input): 
    validation = validators.url(input)
    if validation:
        print('url is valid')
    else:
        print('not a valid url')

