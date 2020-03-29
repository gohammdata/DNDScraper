from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://dnd5e.wikidot.com" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(class_= "col-sm-2").find("a").attrs['href'])
    except AttributeError:
        print("Grabbing the next available link for you John!")

    for link in bsObj.findAll("a", href =re.compile("^(/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #Just encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                print("Added New Page! Not to the SQL yet cuz I'm not a madman")
                getLinks(newPage)
getLinks("")
