import csv
import urllib.request
from bs4 import BeautifulSoup
import os, os.path, csv
from bs4 import NavigableString

fakeurl = "http://www.fakingnews.com/category/india"
page = urllib.request.urlopen(fakeurl)

# print (page)
soup = BeautifulSoup(page, "lxml")
# print (soup.prettyfy())
delrname = soup.find('article', class_='col-lg-9 col-md-8')
# print (delrname)
# domain1 = delrname.li
# print (domain1)
for name in delrname:
    try:
        print (name.text)
    except AttributeError:
        pass
