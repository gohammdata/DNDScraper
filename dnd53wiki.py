from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
def getClasses(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        classes = for link in bsObj.find("div", {class_= "col-sm-2"}).findAll("a",
        href=re.compile("^(/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            
    except AttributeError as e:
        return None
    return classes
classes = getClasses("http://dnd5e.wikidot.com")
if all == None:
    print("Classes could not be found")
else:
    print(classes)
