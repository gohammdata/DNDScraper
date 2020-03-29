# # -*- coding: utf-8 -*-
import scrapy
from ..items import RacelistItem

class DndwikiSpider(scrapy.Spider):
    def store(name, mylinks):
        curr.execute("INSERT INTO dndrtable (name, mylinks) VALUES (\"%s\", \"%s\")",
        (name, mylinks))
    name = 'dndwiki'
    allowed_domains = ['dnd5e.wikidot.com']
    start_urls = ['http://dnd5e.wikidot.com/']

    #Store function for the data to correct area of TABLE


    def parse(self, response):
        #Check connection to http
        print("----------\n")
        print("HTTP STATUS: " +str(response.status))
        print(response.css("title::text").get())
        print("----------\n")
        #Declare what to find
        allReferences = response.css("p > a")
        for race in allReferences:
            #assign the result of the link and text to string variables
            link = race.css("a::attr(href)").get()
            newReference = race.css("a::text").get()
            #print everything with seperators
            print("=====New References===")
            print(link)
            print(newReference)
            print("-----------------\n")
            #store into MYSQL
            store(newReference, link)
            cur.execute("SELECT * FROM dndrtable")
            #assign to RaceListItem's class
            items = RacelistItem()
            items['newReference'] = newReference
            items ['link'] = link
            #yield the class data
            yield items
curr.close()
conn.close()
