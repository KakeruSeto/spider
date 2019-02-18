# -*- coding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):

    name = "url"
    start_urls = [
        "https://www.gakkou.net/daigaku/src/?srcmode=gkm&gkm=09010",
    ]

    def parse(self, response):
        for quote in response.css("body"):
            yield{
                "URL": response.css(".osglink02 a::attr(href)").extract(),
            }

        next_page = response.css("a:contains('次へ')::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)

    custom_settings = {
        "DOWNLOAD_DELAY": 2.0,
    }
