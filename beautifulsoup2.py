# Note - this code must run in Python 2.x and you must download
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')

comments_lst = list()
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:' ,tag 
    print 'Length:', len(tag)
    comments_lst.append(int(tag.contents[0]))

print comments_lst
print "SUM:", sum(comments_lst)
    

    

    
