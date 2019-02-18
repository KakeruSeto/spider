Last login: Mon Sep  3 13:15:59 on ttys000
imainoMacBook-Air:~ imai$ ls
Applications		Dropbox			Music
Desktop			Dropbox (Blanciel)	Pictures
Documents		Library			Public
Downloads		Movies
imainoMacBook-Air:~ imai$ cd Desktop/
imainoMacBook-Air:Desktop imai$ cd tutorial/
imainoMacBook-Air:tutorial imai$ ls
goo.json		quotes-2.html		tochi.json
li.next a		quotes-R6643428.html	tutorial
nomucomu.json		quotes.jl		urls.json
q2.py			quotes.py		urls2.json
quotes-1.html		scrapy.cfg
imainoMacBook-Air:tutorial imai$ ls
goo.json		quotes-2.html		tochi.json
li.next a		quotes-R6643428.html	tutorial
nomucomu.json		quotes.jl		urls.json
q2.py			quotes.py		urls2.json
quotes-1.html		scrapy.cfg
imainoMacBook-Air:tutorial imai$ ls
goo.json		quotes-2.html		tochi.json
li.next a		quotes-R6643428.html	tutorial
nomucomu.json		quotes.jl		urls.json
q2.py			quotes.py		urls2.json
quotes-1.html		scrapy.cfg
imainoMacBook-Air:tutorial imai$ scrapy shell'https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html'
Scrapy 1.5.1 - project: tutorial

Unknown command: shellhttps://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html

Use "scrapy" to see available commands
imainoMacBook-Air:tutorial imai$ scrapy shell 'https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html'
2018-09-03 14:09:58 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: tutorial)
2018-09-03 14:09:58 [scrapy.utils.log] INFO: Versions: lxml 4.2.4.0, libxml2 2.9.8, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 26 2018, 19:50:54) - [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Darwin-16.7.0-x86_64-i386-64bit
2018-09-03 14:09:58 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0, 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2018-09-03 14:09:58 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage']
2018-09-03 14:09:58 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-09-03 14:09:58 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-09-03 14:09:58 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-09-03 14:09:58 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6024
2018-09-03 14:09:58 [scrapy.core.engine] INFO: Spider opened
2018-09-03 14:09:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/robots.txt> (referer: None)
2018-09-03 14:10:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x108756b70>
[s]   item       {}
[s]   request    <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html>
[s]   response   <200 https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html>
[s]   settings   <scrapy.settings.Settings object at 0x1094fb828>
[s]   spider     <DefaultSpider 'default' at 0x10a012400>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> response.css("h1_title_box-type h1::text").extract()
[]
>>> >>> response.css("h1").extract()
['<h1>東京都青梅市富岡２丁目 東青梅駅 土地 物件詳細</h1>']
>>> response.css("h1::text").extract()
['東京都青梅市富岡２丁目 東青梅駅 土地 物件詳細']
>>> response.css("h1::text").extract()
['東京都青梅市富岡２丁目 東青梅駅 土地 物件詳細']
>>> esponse.css("th:contains('価格') + td").xpath('string()').extract_first()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'esponse' is not defined
>>> esponse.css("th:contains('価格')td::text).extract()h 
  File "<console>", line 1
    esponse.css("td::text).extract()h　).extract_first()
                                     　                ^
SyntaxError: EOL while scanning string literal
>>> esponse.css("td::text).extract()
  File "<console>", line 1
    esponse.css("td::text).extract()
                                   ^
SyntaxError: EOL while scanning string literal
>>> esponse.css("th:contains('価格') +td::text").extract()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'esponse' is not defined
>>> esponse.css("th:contains('価格')").extract()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'esponse' is not defined
>>> response.css("th:contains('価格')").extract()
['<th><strong>価格</strong></th>', '<th class="title06">価格</th>']
>>> response.css("th:contains('価格') + td").xpath('string()').extract_first()
'\n        300万円\n      '
>>> response.css("th:contains('価格')td::text").extract()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/http/response/text.py", line 122, in css
    return self.selector.css(query)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/selector.py", line 262, in css
    return self.xpath(self._css2xpath(query))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/selector.py", line 265, in _css2xpath
    return self._csstranslator.css_to_xpath(query)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/csstranslator.py", line 109, in css_to_xpath
    return super(HTMLTranslator, self).css_to_xpath(css, prefix)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/xpath.py", line 192, in css_to_xpath
    for selector in parse(css))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 355, in parse
    return list(parse_selector_group(stream))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 368, in parse_selector_group
    yield Selector(*parse_selector(stream))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 376, in parse_selector
    result, pseudo_element = parse_simple_selector(stream)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 475, in parse_simple_selector
    "Expected selector, got %s" % (peek,))
  File "<string>", line None
cssselect.parser.SelectorSyntaxError: Expected selector, got <IDENT 'td' at 17>
>>> response.css("th:contains('価格') td").extract()
[]
>>> response.css("th:contains('価格') ").extract()
['<th><strong>価格</strong></th>', '<th class="title06">価格</th>']
>>> response.css("th:contains('価格')td::text").extract()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/http/response/text.py", line 122, in css
    return self.selector.css(query)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/selector.py", line 262, in css
    return self.xpath(self._css2xpath(query))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/selector.py", line 265, in _css2xpath
    return self._csstranslator.css_to_xpath(query)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/parsel/csstranslator.py", line 109, in css_to_xpath
    return super(HTMLTranslator, self).css_to_xpath(css, prefix)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/xpath.py", line 192, in css_to_xpath
    for selector in parse(css))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 355, in parse
    return list(parse_selector_group(stream))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 368, in parse_selector_group
    yield Selector(*parse_selector(stream))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 376, in parse_selector
    result, pseudo_element = parse_simple_selector(stream)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cssselect/parser.py", line 475, in parse_simple_selector
    "Expected selector, got %s" % (peek,))
  File "<string>", line None
cssselect.parser.SelectorSyntaxError: Expected selector, got <IDENT 'td' at 17>
>>> "3.土地面積":response.css("th:contains('土地面積') + td").xpath('string()').extract_first()
  File "<console>", line 1
SyntaxError: illegal target for annotation
>>> "3.土地面積":response.css("th:contains('土地面積') + td").xpath('string()').extract_first()
  File "<console>", line 1
SyntaxError: illegal target for annotation
>>> response.css("th.value02")
[]
>>> response.css("th.value02").extract()
[]
>>> response.css("tbody").extract()
['<tbody>\n    <tr class="detail_outline-data-sep detail_outline-data-price">\n      <th><strong>価格</strong></th>\n      <td colspan="3">\n        <span>300</span>万円\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>坪単価</strong></th>\n      <td colspan="3">5.1万円</td>\n    </tr>\n    <tr class="detail_outline-data-sep2">\n      <th><strong>交通</strong></th>\n      <td colspan="3">\n\n<ul class="access-list">\n  <li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>\n</ul>\n<ul class="detail_icon-list">\n  <li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>\n</ul>\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep3">\n      <th><strong>所在地</strong></th>\n      <td colspan="3">\n東京都青梅市富岡２丁目<a href="#map" class="detail_outline-map">周辺地図</a>\n<ul class="detail_icon-list">\n<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>\n<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>\n</ul>\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep3">\n      <th><strong>土地面積</strong></th>\n      <td colspan="3">198m<sup>2</sup></td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>用途地域</strong></th>\n      <td>無指定</td>\n      <th><strong>建築条件</strong></th>\n      <td>無</td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>建ぺい率</strong></th>\n      <td>40％</td>\n      <th><strong>容積率</strong></th>\n      <td>80％</td>\n    </tr>\n  </tbody>']
>>> response.css("tbody").extract()
['<tbody>\n    <tr class="detail_outline-data-sep detail_outline-data-price">\n      <th><strong>価格</strong></th>\n      <td colspan="3">\n        <span>300</span>万円\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>坪単価</strong></th>\n      <td colspan="3">5.1万円</td>\n    </tr>\n    <tr class="detail_outline-data-sep2">\n      <th><strong>交通</strong></th>\n      <td colspan="3">\n\n<ul class="access-list">\n  <li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>\n</ul>\n<ul class="detail_icon-list">\n  <li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>\n</ul>\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep3">\n      <th><strong>所在地</strong></th>\n      <td colspan="3">\n東京都青梅市富岡２丁目<a href="#map" class="detail_outline-map">周辺地図</a>\n<ul class="detail_icon-list">\n<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>\n<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>\n</ul>\n      </td>\n    </tr>\n    <tr class="detail_outline-data-sep3">\n      <th><strong>土地面積</strong></th>\n      <td colspan="3">198m<sup>2</sup></td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>用途地域</strong></th>\n      <td>無指定</td>\n      <th><strong>建築条件</strong></th>\n      <td>無</td>\n    </tr>\n    <tr class="detail_outline-data-sep4">\n      <th><strong>建ぺい率</strong></th>\n      <td>40％</td>\n      <th><strong>容積率</strong></th>\n      <td>80％</td>\n    </tr>\n  </tbody>']
>>> response.css("table.rent_detail_table2").extract()
[]
>>> response.css("table.rent_detail_table_02").extract()
['<table class="rent_detail_table_02" summary="青梅線 東青梅の詳細情報です">\r\n<tr>\r\n<th class="title06">価格</th>\r\n<td class="value02" colspan="3">300万円 <ul class="detail_icon-list detail_icon-list-inline"><a href="#loan">ローンシミュレーション</a></ul></td>\r\n</tr>\r\n<tr>\r\n<th class="title06">土地面積</th>\r\n<td class="value02" width="37%">198m<sup>2</sup></td>\r\n<th class="title06">坪単価</th>\r\n<td class="value02" width="37%">5.1万円</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">所在地</th>\r\n<td class="value02" colspan="3">\r\n東京都青梅市富岡２丁目<a href="#map" class="detail_outline-map">周辺地図</a>\n<ul class="detail_icon-list detail_icon-list-inline">\n<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>\n<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>\n</ul>\n</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">交通</th>\r\n<td class="value02" colspan="3">\r\n\n<ul class="access-list">\n  <li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>\n</ul>\n<ul class="detail_icon-list">\n  <li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>\n</ul>\n</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">土地権利</th>\r\n<td class="value02">所有権</td>\r\n<th class="title06">都市計画</th>\r\n<td class="value02">調整区域</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">借地期間・地代</th>\r\n<td class="value02">\xa0</td>\r\n<th class="title06">用途地域</th>\r\n<td class="value02">無指定</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">建築条件</th>\r\n<td class="value02">なし</td>\r\n<th class="title06">建ぺい率/容積率</th>\r\n<td class="value02">40％\xa0/\xa080％</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">私道面積</th>\r\n<td class="value02">\xa0</td>\r\n<th class="title06">地目</th>\r\n<td class="value02">雑種地</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">接道状況</th>\r\n<td class="value02">\r\n南東6ｍ公道</td>\r\n<th class="title06">引渡時期</th>\r\n<td class="value02">\r\n即時</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">現況</th>\r\n<td class="value02">更地</td>\r\n<th class="title06">条件等</th>\r\n<td class="value02"></td>\r\n</tr>\r\n\r\n</table>', '<table class="rent_detail_table_02" summary="青梅線 東青梅の設備情報です">\r\n<tr>\r\n<th class="title06" width="17%">建築条件</th>\r\n<td class="value02 TAC" width="15%">なし</td>\r\n<th class="title06" width="17%">1種低層地域</th>\r\n<td class="TAC" width="15%">-</td>\r\n<th class="title06" width="17%">売主・代理</th>\r\n<td class="TAC" width="15%">-</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">本下水</th>\r\n<td class="TAC">-</td>\r\n<th class="title06">都市ガス</th>\r\n<td class="TAC">-</td>\r\n<th class="title06">角地</th>\r\n<td class="TAC">-</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">即引渡し可</th>\r\n<td class="TAC">○</td>\r\n<th class="title06">\xa0</th>\r\n<td class="TAC">\xa0</td>\r\n<th class="title06">\xa0</th>\r\n<td class="TAC">\xa0</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">設備</th>\r\n<td colspan="5" class="value02">\r\n\xa0</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">備考</th>\r\n<td colspan="5" class="value02">【物件周辺の生活情報】<br>・学校<br>第七小学校（3,582m）、第六中学校（3,051m）<br>・買い物<br>スーパー（6,500m）<br>・その他施設<br>銀行（7,040m）、カインズホーム青梅インター店（6,370m）<br>［物件コード］１２３００１－４４０６、建築不可\u3000【設備・特記事項備考】建築条件なし<br>地勢：平坦<br>法令等制限：建築基準法第４３条但書許可要<br>土地面積：公薄</td>\r\n</tr>\r\n<tr>\r\n<th class="title06">特記事項</th>\r\n<td colspan="5" class="value02">\r\n\xa0</td>\r\n</tr>\r\n</table>']
>>> response.css("table.rent_detail_table_02 tr").extract()
['<tr>\r\n<th class="title06">価格</th>\r\n<td class="value02" colspan="3">300万円 <ul class="detail_icon-list detail_icon-list-inline"><a href="#loan">ローンシミュレーション</a></ul></td>\r\n</tr>', '<tr>\r\n<th class="title06">土地面積</th>\r\n<td class="value02" width="37%">198m<sup>2</sup></td>\r\n<th class="title06">坪単価</th>\r\n<td class="value02" width="37%">5.1万円</td>\r\n</tr>', '<tr>\r\n<th class="title06">所在地</th>\r\n<td class="value02" colspan="3">\r\n東京都青梅市富岡２丁目<a href="#map" class="detail_outline-map">周辺地図</a>\n<ul class="detail_icon-list detail_icon-list-inline">\n<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>\n<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>\n</ul>\n</td>\r\n</tr>', '<tr>\r\n<th class="title06">交通</th>\r\n<td class="value02" colspan="3">\r\n\n<ul class="access-list">\n  <li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>\n</ul>\n<ul class="detail_icon-list">\n  <li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>\n</ul>\n</td>\r\n</tr>', '<tr>\r\n<th class="title06">土地権利</th>\r\n<td class="value02">所有権</td>\r\n<th class="title06">都市計画</th>\r\n<td class="value02">調整区域</td>\r\n</tr>', '<tr>\r\n<th class="title06">借地期間・地代</th>\r\n<td class="value02">\xa0</td>\r\n<th class="title06">用途地域</th>\r\n<td class="value02">無指定</td>\r\n</tr>', '<tr>\r\n<th class="title06">建築条件</th>\r\n<td class="value02">なし</td>\r\n<th class="title06">建ぺい率/容積率</th>\r\n<td class="value02">40％\xa0/\xa080％</td>\r\n</tr>', '<tr>\r\n<th class="title06">私道面積</th>\r\n<td class="value02">\xa0</td>\r\n<th class="title06">地目</th>\r\n<td class="value02">雑種地</td>\r\n</tr>', '<tr>\r\n<th class="title06">接道状況</th>\r\n<td class="value02">\r\n南東6ｍ公道</td>\r\n<th class="title06">引渡時期</th>\r\n<td class="value02">\r\n即時</td>\r\n</tr>', '<tr>\r\n<th class="title06">現況</th>\r\n<td class="value02">更地</td>\r\n<th class="title06">条件等</th>\r\n<td class="value02"></td>\r\n</tr>', '<tr>\r\n<th class="title06" width="17%">建築条件</th>\r\n<td class="value02 TAC" width="15%">なし</td>\r\n<th class="title06" width="17%">1種低層地域</th>\r\n<td class="TAC" width="15%">-</td>\r\n<th class="title06" width="17%">売主・代理</th>\r\n<td class="TAC" width="15%">-</td>\r\n</tr>', '<tr>\r\n<th class="title06">本下水</th>\r\n<td class="TAC">-</td>\r\n<th class="title06">都市ガス</th>\r\n<td class="TAC">-</td>\r\n<th class="title06">角地</th>\r\n<td class="TAC">-</td>\r\n</tr>', '<tr>\r\n<th class="title06">即引渡し可</th>\r\n<td class="TAC">○</td>\r\n<th class="title06">\xa0</th>\r\n<td class="TAC">\xa0</td>\r\n<th class="title06">\xa0</th>\r\n<td class="TAC">\xa0</td>\r\n</tr>', '<tr>\r\n<th class="title06">設備</th>\r\n<td colspan="5" class="value02">\r\n\xa0</td>\r\n</tr>', '<tr>\r\n<th class="title06">備考</th>\r\n<td colspan="5" class="value02">【物件周辺の生活情報】<br>・学校<br>第七小学校（3,582m）、第六中学校（3,051m）<br>・買い物<br>スーパー（6,500m）<br>・その他施設<br>銀行（7,040m）、カインズホーム青梅インター店（6,370m）<br>［物件コード］１２３００１－４４０６、建築不可\u3000【設備・特記事項備考】建築条件なし<br>地勢：平坦<br>法令等制限：建築基準法第４３条但書許可要<br>土地面積：公薄</td>\r\n</tr>', '<tr>\r\n<th class="title06">特記事項</th>\r\n<td colspan="5" class="value02">\r\n\xa0</td>\r\n</tr>']
>>> response.css("table.rent_detail_table_02 tr td").extract()
['<td class="value02" colspan="3">300万円 <ul class="detail_icon-list detail_icon-list-inline"><a href="#loan">ローンシミュレーション</a></ul></td>', '<td class="value02" width="37%">198m<sup>2</sup></td>', '<td class="value02" width="37%">5.1万円</td>', '<td class="value02" colspan="3">\r\n東京都青梅市富岡２丁目<a href="#map" class="detail_outline-map">周辺地図</a>\n<ul class="detail_icon-list detail_icon-list-inline">\n<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>\n<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>\n</ul>\n</td>', '<td class="value02" colspan="3">\r\n\n<ul class="access-list">\n  <li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>\n</ul>\n<ul class="detail_icon-list">\n  <li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>\n</ul>\n</td>', '<td class="value02">所有権</td>', '<td class="value02">調整区域</td>', '<td class="value02">\xa0</td>', '<td class="value02">無指定</td>', '<td class="value02">なし</td>', '<td class="value02">40％\xa0/\xa080％</td>', '<td class="value02">\xa0</td>', '<td class="value02">雑種地</td>', '<td class="value02">\r\n南東6ｍ公道</td>', '<td class="value02">\r\n即時</td>', '<td class="value02">更地</td>', '<td class="value02"></td>', '<td class="value02 TAC" width="15%">なし</td>', '<td class="TAC" width="15%">-</td>', '<td class="TAC" width="15%">-</td>', '<td class="TAC">-</td>', '<td class="TAC">-</td>', '<td class="TAC">-</td>', '<td class="TAC">○</td>', '<td class="TAC">\xa0</td>', '<td class="TAC">\xa0</td>', '<td colspan="5" class="value02">\r\n\xa0</td>', '<td colspan="5" class="value02">【物件周辺の生活情報】<br>・学校<br>第七小学校（3,582m）、第六中学校（3,051m）<br>・買い物<br>スーパー（6,500m）<br>・その他施設<br>銀行（7,040m）、カインズホーム青梅インター店（6,370m）<br>［物件コード］１２３００１－４４０６、建築不可\u3000【設備・特記事項備考】建築条件なし<br>地勢：平坦<br>法令等制限：建築基準法第４３条但書許可要<br>土地面積：公薄</td>', '<td colspan="5" class="value02">\r\n\xa0</td>']
>>> response.css("table.rent_detail_table_02 tr td::text").extract()
['300万円 ', '198m', '5.1万円', '\r\n東京都青梅市富岡２丁目', '\n', '\n', '\r\n\n', '\n', '\n', '所有権', '調整区域', '\xa0', '無指定', 'なし', '40％\xa0/\xa080％', '\xa0', '雑種地', '\r\n南東6ｍ公道', '\r\n即時', '更地', 'なし', '-', '-', '-', '-', '-', '○', '\xa0', '\xa0', '\r\n\xa0', '【物件周辺の生活情報】', '・学校', '第七小学校（3,582m）、第六中学校（3,051m）', '・買い物', 'スーパー（6,500m）', '・その他施設', '銀行（7,040m）、カインズホーム青梅インター店（6,370m）', '［物件コード］１２３００１－４４０６、建築不可\u3000【設備・特記事項備考】建築条件なし', '地勢：平坦', '法令等制限：建築基準法第４３条但書許可要', '土地面積：公薄', '\r\n\xa0']
>>> response.css("table.rent_detail_table_02 th:contains('価格') tr td::text").extract()
[]
>>> response.css("table.rent_detail_table_02 th:contains('価格')+tr td::text").extract()
[]
>>> response.css("table.rent_detail_table_02+th:contains('価格')+tr td::text").extract()
[]
>>> response.css("table.rent_detail_table_02+th:contains('価格')+ td::text").extract()
[]
>>> response.css("table.rent_detail_table_02 + th:contains('価格') + td::text").extract()
[]
>>> response.css("table.rent_detail_table_02  th:contains('価格') + td::text").extract()
['300万円 ']
>>> response.css("table.rent_detail_table_02  th:contains('土地面積') + td::t  t").extract()
['198m']
>>> response.css("table.rent_detail_table_02  th:contains('坪単価') + td::text").extract()
['5.1万円']
>>> "5.所在地":response.css("table.rent_detail_table_02  th:contains('所在地') + td::text").extract(),
  File "<console>", line 1
    "5.所在地":response.css("table.rent_detail_table_02  th:contains('所在地') + td::text").extract(),
                                                                                               ^
SyntaxError: invalid syntax
>>>                             "6.交通":response.css("table.rent_detail_table_02  th:contains('交通') + td::text").extract(),
  File "<console>", line 1
    "6.交通":response.css("table.rent_detail_table_02  th:contains('交通') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "7.土地権利":response.css("th:contains('土地権利') + td::text").extract(),
  File "<console>", line 1
    "7.土地権利":response.css("th:contains('土地権利') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "8.都市計画":response.css("table.rent_detail_table_02  th:contains('都市計画') + td::text").extract(),
  File "<console>", line 1
    "8.都市計画":response.css("table.rent_detail_table_02  th:contains('都市計画') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "9.借地期間・地代":response.css("table.rent_detail_table_02  th:contains('借地期間・地代') + td::text").extract(),
  File "<console>", line 1
    "9.借地期間・地代":response.css("table.rent_detail_table_02  th:contains('借地期間・地代') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "10.用途地域":response.css("table.rent_detail_table_02  th:contains('用途地域') + td::text").extract(),
  File "<console>", line 1
    "10.用途地域":response.css("table.rent_detail_table_02  th:contains('用途地域') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "11.建築条件":response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract(),
  File "<console>", line 1
    "11.建築条件":response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "12.建ぺい率/容積率":response.css("table.rent_detail_table_02  th:contains('建ぺい率/容積率') + td::text").extract(),
  File "<console>", line 1
    "12.建ぺい率/容積率":response.css("table.rent_detail_table_02  th:contains('建ぺい率/容積率') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "13.私道面積":response.css("table.rent_detail_table_02  th:contains('私道面積') + td::text").extract(),
  File "<console>", line 1
    "13.私道面積":response.css("table.rent_detail_table_02  th:contains('私道面積') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "14.地目":response.css("table.rent_detail_table_02  th:contains('地目') + td::text").extract(),
  File "<console>", line 1
    "14.地目":response.css("table.rent_detail_table_02  th:contains('地目') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "15.接道状況":response.css("table.rent_detail_table_02  th:contains('接道状況') + td::text").extract(),
  File "<console>", line 1
    "15.接道状況":response.css("table.rent_detail_table_02  th:contains('接道状況') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "16.引渡時期":response.css("table.rent_detail_table_02  th:contains('引渡時期') + td::text").extract(),
  File "<console>", line 1
    "16.引渡時期":response.css("table.rent_detail_table_02  th:contains('引渡時期') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "17.現況":response.css("table.rent_detail_table_02  th:contains('現況') + td::text").extract(),
  File "<console>", line 1
    "17.現況":response.css("table.rent_detail_table_02  th:contains('現況') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                             "18.条件等":response.css("table.rent_detail_table_02  th:contains('条件等') + td::text").extract(),
  File "<console>", line 1
    "18.条件等":response.css("table.rent_detail_table_02  th:contains('条件等') + td::text").extract(),
    ^
IndentationError: unexpected indent
>>>                 
>>> response.css("table.rent_detail_table_02  th:contains('所在地') + td::text").extract()
['\r\n東京都青梅市富岡２丁目', '\n', '\n']
>>> response.css("table.rent_detail_table_02  th:contains('交通') + td::text").extract(),
(['\r\n\n', '\n', '\n'],)
>>> response.css("th:contains('土地権利') + td::text").extract()
['所有権']
>>> response.css("table.rent_detail_table_02  th:contains('都市計画') + td::text").extract()
['調整区域']
>>> response.css("table.rent_detail_table_02  th:contains('借地期間・地代') + td::text").extract()
['\xa0']
>>> response.css("table.rent_detail_table_02  th:contains('用途地域') + td::text").extract()
['無指定']
>>> response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract()
['なし', 'なし']
>>> response.css("table.rent_detail_table_02  th:contains('建ぺい率/容積率') + td::text").extract()
['40％\xa0/\xa080％']
>>> response.css("table.rent_detail_table_02  th:contains('私道面積') + td::text").extract()
['\xa0']
>>> response.css("table.rent_detail_table_02  th:contains('地目') + td::text").extract()
['雑種地']
>>> response.css("table.rent_detail_table_02  th:contains('接道状況') + td::text").extract()
['\r\n南東6ｍ公道']
>>> response.css("table.rent_detail_table_02  th:contains('引渡時期') + td::text").extract()
['\r\n即時']
>>> response.css("table.rent_detail_table_02  th:contains('現況') + td::text").extract()
['更地']
>>> response.css("table.rent_detail_table_02  th:contains('条件等') + td::text").extract()
[]
>>> exit()
imainoMacBook-Air:tutorial imai$ 
imainoMacBook-Air:tutorial imai$ ls
goo.json		quotes-2.html		tochi.json
li.next a		quotes-R6643428.html	tutorial
nomucomu.json		quotes.jl		urls.json
q2.py			quotes.py		urls2.json
quotes-1.html		scrapy.cfg
imainoMacBook-Air:tutorial imai$ scrapy crawl goo2 -o goo2.json
2018-09-03 15:19:55 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: tutorial)
2018-09-03 15:19:55 [scrapy.utils.log] INFO: Versions: lxml 4.2.4.0, libxml2 2.9.8, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 26 2018, 19:50:54) - [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Darwin-16.7.0-x86_64-i386-64bit
2018-09-03 15:19:55 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'DOWNLOAD_DELAY': 6.0, 'FEED_FORMAT': 'json', 'FEED_URI': 'goo2.json', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2018-09-03 15:19:55 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2018-09-03 15:19:55 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-09-03 15:19:55 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-09-03 15:19:55 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-09-03 15:19:55 [scrapy.core.engine] INFO: Spider opened
2018-09-03 15:19:55 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2018-09-03 15:19:55 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-09-03 15:19:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/robots.txt> (referer: None)
2018-09-03 15:20:04 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html> (referer: None)
2018-09-03 15:20:04 [scrapy.core.scraper] ERROR: Spider error processing <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html> (referer: None)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/utils/defer.py", line 102, in iter_errback
    yield next(it)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/spidermiddlewares/offsite.py", line 30, in process_spider_output
    for x in result:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/spidermiddlewares/referer.py", line 339, in <genexpr>
    return (_set_referer(r) for r in result or ())
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/spidermiddlewares/urllength.py", line 37, in <genexpr>
    return (r for r in result or () if _filter(r))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/spidermiddlewares/depth.py", line 58, in <genexpr>
    return (r for r in result or () if _filter(r))
  File "/Users/imai/Desktop/tutorial/tutorial/spiders/goo2.py", line 36, in parse
    "19.建築条件":response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract_second(),
AttributeError: 'SelectorList' object has no attribute 'extract_second'
2018-09-03 15:20:04 [scrapy.core.engine] INFO: Closing spider (finished)
2018-09-03 15:20:04 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 698,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 19814,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 9, 3, 6, 20, 4, 714172),
 'log_count/DEBUG': 3,
 'log_count/ERROR': 1,
 'log_count/INFO': 7,
 'memusage/max': 46530560,
 'memusage/startup': 46526464,
 'response_received_count': 2,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'spider_exceptions/AttributeError': 1,
 'start_time': datetime.datetime(2018, 9, 3, 6, 19, 55, 360172)}
2018-09-03 15:20:04 [scrapy.core.engine] INFO: Spider closed (finished)
imainoMacBook-Air:tutorial imai$ response.css("table.rent_detail_table_02  th:contains('交通') + li::text").extract()
-bash: syntax error near unexpected token `"table.rent_detail_table_02  th:contains('交通') + li::text"'
imainoMacBook-Air:tutorial imai$ response.css("table.rent_detail_table_02  th:contains('交通') + li").extract()
-bash: syntax error near unexpected token `"table.rent_detail_table_02  th:contains('交通') + li"'
imainoMacBook-Air:tutorial imai$ response.css("table.rent_detail_table_02").extract()
-bash: syntax error near unexpected token `"table.rent_detail_table_02"'
imainoMacBook-Air:tutorial imai$ ls
goo.json		quotes-1.html		scrapy.cfg
goo2.json		quotes-2.html		tochi.json
li.next a		quotes-R6643428.html	tutorial
nomucomu.json		quotes.jl		urls.json
q2.py			quotes.py		urls2.json
imainoMacBook-Air:tutorial imai$ scrapy shell 'https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html'
2018-09-03 15:27:55 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: tutorial)
2018-09-03 15:27:55 [scrapy.utils.log] INFO: Versions: lxml 4.2.4.0, libxml2 2.9.8, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 26 2018, 19:50:54) - [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Darwin-16.7.0-x86_64-i386-64bit
2018-09-03 15:27:55 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0, 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2018-09-03 15:27:55 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage']
2018-09-03 15:27:55 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-09-03 15:27:55 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-09-03 15:27:55 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-09-03 15:27:55 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-09-03 15:27:55 [scrapy.core.engine] INFO: Spider opened
2018-09-03 15:27:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/robots.txt> (referer: None)
2018-09-03 15:27:56 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x104a9abe0>
[s]   item       {}
[s]   request    <GET https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html>
[s]   response   <200 https://house.goo.ne.jp/buy/la/detail/4/13205/83550003616/8355/x483550003616.html>
[s]   settings   <scrapy.settings.Settings object at 0x1058d2710>
[s]   spider     <DefaultSpider 'default' at 0x10640f550>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> response.css("table.rent_detail_table_02  th:contains('交通') + li::text").extract()
[]
>>> response.css("table.rent_detail_table_02  th:contains('交通') + li").extract()
[]
>>> response.css("table.rent_detail_table_02  li").extract() 
['<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>', '<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>', '<li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>', '<li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>']
>>> response.css("table.rent_detail_table_02 ul  li").extract()
['<li><a href="/chiiki/kurashi/tokyo/13205.html">青梅市の行政データ</a></li>', '<li><a href="/chiiki/souba/tokyo/area/13205.html">青梅市周辺の家賃相場</a></li>', '<li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>', '<li><a href="/chiiki/town/tokyo/ensen/185/2185120/">東青梅駅のクチコミ情報</a></li>']
>>> response.css("table.rent_detail_table_02 ul.access-list  li").extract()
['<li>青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分<a href="https://transit.goo.ne.jp/?off_st=%E6%9D%B1%E9%9D%92%E6%A2%85&amp;off_st_id=130510" class="detail_outline-transfer" target="_blank">乗換案内</a></li>']
>>> response.css("table.rent_detail_table_02 ul.access-list  li::text").extract()
['青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分']
>>> response.css("table.rent_detail_table_02 ul.access-list  li::text").extract()
['青梅線\xa0東青梅駅\xa0バス25分/「成木一丁目四ツ角」バス停\xa0停歩8分']
>>> response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract_second(),
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'SelectorList' object has no attribute 'extract_second'
>>> response.css("table.rent_detail_table_02  th:contains('建築条件') + td::text").extract_second()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'SelectorList' object has no attribute 'extract_second'
>>> response.css("table.rent_detail_table_02  th:contains('条件等') + td::text").extract()
[]
>>> response.css("table.rent_detail_table_02  th:contains('１種低層地域') + td::text").extract()
[]
>>> response.css("table.rent_detail_table_02  th:contains('売主・代理') + td::text").extract()
['-']
>>> response.css("table.rent_detail_table_02  th:contains('本下水') + td::text").extract()
['-']
>>> response.css("table.rent_detail_table_02  th:contains('都市ガス') + td::text").extract()
['-']
>>> response.css("table.rent_detail_table_02  th:contains('角地') + td::text").extract()
['-']
>>> response.css("table.rent_detail_table_02  th:contains('即引渡し可') + td::text").extract()
['○']
>>> response.css("table.rent_detail_table_02  th:contains('設備') + td::text").extract()
['\r\n\xa0']
>>> response.css("table.rent_detail_table_02  th:contains('備考') + td::text").extract()
['【物件周辺の生活情報】', '・学校', '第七小学校（3,582m）、第六中学校（3,051m）', '・買い物', 'スーパー（6,500m）', '・その他施設', '銀行（7,040m）、カインズホーム青梅インター店（6,370m）', '［物件コード］１２３００１－４４０６、建築不可\u3000【設備・特記事項備考】建築条件なし', '地勢：平坦', '法令等制限：建築基準法第４３条但書許可要', '土地面積：公薄']
>>> response.css("table.rent_detail_table_02  th:contains('特記事項') + td::text").extract()
['\r\n\xa0']
>>> response.css("table.rent_detail_table_02  th:contains('1種低層地域') + td::text").extract()
['-']
>>> 
