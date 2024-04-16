# A Module is basically a file containing a set of function to include in your application,
# There are core python modules, modules you can install using the pip package manager
# including ( Django ) as well know custom module

import datetime
from datetime import date
import time
from time import time

today= date.today()

print(today)

timestamp = time()
print(timestamp)

# import pip module
# install camelcase : pip3 install camelcase

import camelcase
from camelcase import CamelCase

c = CamelCase()

print (c.hump('hello there world'))

# Custom Module Validator
import validator
from validator import validate_email

test = 'test@test.com'

if validate_email(test):
    print(f'Email is Valid')
else:
    print(f'Email is not Valid')