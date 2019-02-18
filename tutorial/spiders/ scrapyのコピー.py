# -*- coding: utf-8 -*-

import scrapy
from datetime import datetime


class QuotesSpider(scrapy.Spider):
    name = "gak2"

    def start_requests(self):
        urls = [
"https://www.gakkou.net/daigaku/view/index_10583.html", "https://www.gakkou.net/daigaku/view/index_10147.html", "https://www.gakkou.net/daigaku/view/index_10095.html", "https://www.gakkou.net/daigaku/view/index_10517.html", "https://www.gakkou.net/daigaku/view/index_10322.html", "https://www.gakkou.net/daigaku/view/index_10398.html", "https://www.gakkou.net/daigaku/view/index_10339.html", "https://www.gakkou.net/daigaku/view/index_10258.html", "https://www.gakkou.net/daigaku/view/index_10536.html", "https://www.gakkou.net/daigaku/view/index_10434.html", "https://www.gakkou.net/daigaku/view/index_10224.html", "https://www.gakkou.net/daigaku/view/index_10209.html", "https://www.gakkou.net/daigaku/view/index_10268.html", "https://www.gakkou.net/daigaku/view/index_10400.html", "https://www.gakkou.net/daigaku/view/index_10471.html", "https://www.gakkou.net/daigaku/view/index_10220.html", "https://www.gakkou.net/daigaku/view/index_10370.html", "https://www.gakkou.net/daigaku/view/index_10101.html", "https://www.gakkou.net/daigaku/view/index_10269.html", "https://www.gakkou.net/daigaku/view/index_10680.html", "https://www.gakkou.net/daigaku/view/index_10555.html", "https://www.gakkou.net/daigaku/view/index_10088.html", "https://www.gakkou.net/daigaku/view/index_10448.html", "https://www.gakkou.net/daigaku/view/index_10478.html", "https://www.gakkou.net/daigaku/view/index_10250.html", "https://www.gakkou.net/daigaku/view/index_10255.html", "https://www.gakkou.net/daigaku/view/index_10496.html", "https://www.gakkou.net/daigaku/view/index_10699.html", "https://www.gakkou.net/daigaku/view/index_10459.html", "https://www.gakkou.net/daigaku/view/index_10140.html"

   ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('body'):
            yield{
                "学校名": response.css("th:contains('学校名') + td").xpath('string()').extract_first(),
                "学校区分": response.css("th:contains('学校区分') + td").xpath('string()').extract_first(),
                "設置区分": response.css("th:contains('設置区分') + td").xpath('string()').extract_first(),
                "所在地": response.css("th:contains('所在地') + td").xpath('string()').extract_first(),
                "電話番号": response.css("th:contains('電話番号') + td").xpath('string()').extract_first(),
                "取得時間": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            }

    custom_settings = {
        "DOWNLOAD_DELAY": 3.0,
    }
