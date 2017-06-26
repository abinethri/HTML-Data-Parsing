# Note - this code must run in Python 2.x and you must download
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup('a')

for tag in tags:
    print tag.get('href', None)
           
     