from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://dnd5e.wikidot.com/")
if title == None:
    print("Title could not be found")
else:
    print(title)
