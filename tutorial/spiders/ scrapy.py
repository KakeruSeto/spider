# -*- coding: utf-8 -*-

import scrapy
from datetime import datetime


class QuotesSpider(scrapy.Spider):
    name = "gak"

    def start_requests(self):
        urls = [
            "https://www.gakkou.net/daigaku/view/index_10437.html", "https://www.gakkou.net/daigaku/view/index_10127.html", "https://www.gakkou.net/daigaku/view/index_10031.html", "https://www.gakkou.net/daigaku/view/index_10583.html", "https://www.gakkou.net/daigaku/view/index_10398.html", "https://www.gakkou.net/daigaku/view/index_10322.html", "https://www.gakkou.net/daigaku/view/index_10517.html", "https://www.gakkou.net/daigaku/view/index_10280.html", "https://www.gakkou.net/daigaku/view/index_10015.html", "https://www.gakkou.net/daigaku/view/index_10339.html", "https://www.gakkou.net/daigaku/view/index_10258.html", "https://www.gakkou.net/daigaku/view/index_10036.html", "https://www.gakkou.net/daigaku/view/index_10189.html", "https://www.gakkou.net/daigaku/view/index_10077.html", "https://www.gakkou.net/daigaku/view/index_10214.html", "https://www.gakkou.net/daigaku/view/index_10434.html", "https://www.gakkou.net/daigaku/view/index_10219.html", "https://www.gakkou.net/daigaku/view/index_10309.html", "https://www.gakkou.net/daigaku/view/index_10650.html", "https://www.gakkou.net/daigaku/view/index_10118.html", "https://www.gakkou.net/daigaku/view/index_10224.html", "https://www.gakkou.net/daigaku/view/index_10209.html", "https://www.gakkou.net/daigaku/view/index_10443.html", "https://www.gakkou.net/daigaku/view/index_10471.html", "https://www.gakkou.net/daigaku/view/index_10053.html", "https://www.gakkou.net/daigaku/view/index_10663.html", "https://www.gakkou.net/daigaku/view/index_10065.html", "https://www.gakkou.net/daigaku/view/index_10101.html", "https://www.gakkou.net/daigaku/view/index_10555.html", "https://www.gakkou.net/daigaku/view/index_10617.html", "https://www.gakkou.net/daigaku/view/index_10200.html", "https://www.gakkou.net/daigaku/view/index_10788.html", "https://www.gakkou.net/daigaku/view/index_10087.html", "https://www.gakkou.net/daigaku/view/index_10006.html", "https://www.gakkou.net/daigaku/view/index_10448.html", "https://www.gakkou.net/daigaku/view/index_10335.html", "https://www.gakkou.net/daigaku/view/index_10299.html", "https://www.gakkou.net/daigaku/view/index_10681.html", "https://www.gakkou.net/daigaku/view/index_10478.html", "https://www.gakkou.net/daigaku/view/index_10250.html", "https://www.gakkou.net/daigaku/view/index_10255.html", "https://www.gakkou.net/daigaku/view/index_10496.html", "https://www.gakkou.net/daigaku/view/index_10385.html", "https://www.gakkou.net/daigaku/view/index_10459.html", "https://www.gakkou.net/daigaku/view/index_10007.html", "https://www.gakkou.net/daigaku/view/index_10140.html", "https://www.gakkou.net/daigaku/view/index_10142.html", "https://www.gakkou.net/daigaku/view/index_10028.html", "https://www.gakkou.net/daigaku/view/index_10454.html", "https://www.gakkou.net/daigaku/view/index_10115.html",
"https://www.gakkou.net/daigaku/view/index_10511.html", "https://www.gakkou.net/daigaku/view/index_10052.html"

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
