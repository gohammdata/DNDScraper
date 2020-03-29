# -*- coding: utf-8 -*-
import scrapy


class DndwikiSpider(scrapy.Spider):
    name = 'dndwiki'
    allowed_domains = ['dnd5e.wikidot.com']
    start_urls = ['http://dnd5e.wikidot.com/']

    def parse(self, response):
        print("----------\n")
        print("HTTP STATUS: " +str(response.status))
        print(response.css("title::text").get())
        print("----------\n")
        # item = Article()
            # for titile in response.css('col-sm-2'):
            #     yield {'title': title.css('a ::text').get()}
            #
            # for next_page in response.css('a.next-col-sm-2-link'):
            #     yield response.follow(next_page, self.parse)
