from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
    href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    #Format of revisionn history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&actoin=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+histroyrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    #Finds only the links with class "mw-annouserlink" which has IP addresses and not usernames
    ipAddresses = bsObj.findAll("a", {"class":"mw-annouserlink"})
    addressList = set()
    for ipAdress in ipAddresses:
        addresslist.add(ipAddress.get_text())
    return addresslist

links = getLinks("/wiki/AngularJS")

while(len(links) > 0):
    for link in links:
        print("-----------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)
    newlink = links[random.ranint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
