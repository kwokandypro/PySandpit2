# -*- coding: utf-8 -*-
import scrapy


class MyexampleSpider(scrapy.Spider):
    name = "myexample"
    allowed_domains = ["http://mherman.org/blog/2012/11/05/scraping-web-pages-with-scrapy/#.V49rxaIe2jx"]
    start_urls = (
        'http://www.http://mherman.org/blog/2012/11/05/scraping-web-pages-with-scrapy/#.V49rxaIe2jx/',
    )

    def parse(self, response):
        pass
