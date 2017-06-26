# Note - this code must run in Python 2.x and you must download
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
inp_count = raw_input('Enter count: ')
inp_pos = raw_input('Enter position: ')

new_pos = int(inp_pos)
count = 0
name_lst = list()

while count <= int(inp_count):
    print "Retrieving: ", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    lst = str(soup.find('title').text).split()
    name_lst.append(lst[2])

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[new_pos-1].get('href', None)
    # print tags.contents[0] can be used for getting names 
    count = count + 1

print "Sequence of names: ", name_lst
print "Last name in Sequence: ", name_lst.pop()  
      

    
