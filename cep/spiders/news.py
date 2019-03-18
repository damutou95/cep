# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import scrapy
import re
class NewsSpider(scrapy.Spider):
    name = 'news'
    #allowed_domains = ['sss']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        #'Cookie': '_ga=GA1.3.54805363.1551923779; _gid=GA1.3.1366219062.1551923779; __utmc=268261020; __utmz=268261020.1551923779.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); homepage3=visited; __iid=; __su=0; __RC=-1; __R=0; __tawkuuid=e::cep.com.vn::EP2djJgUdS0LLqE8VQMTeyfOckmSlnVjecykSzwVRYag/oU+SBvO0ZENl1sLdw1q::2; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22fe15fa7faad65c17d3bfe3a0bea5ed30%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22106.122.167.106%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A104%3A%22Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F71.0.3578.98+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1551902160%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22site_lang%22%3Bs%3A2%3A%22vi%22%3B%7D23034f0290838dcff32c6cb08d5be7bf; __utma=268261020.54805363.1551923779.1551923779.1551927447.2; __utmt=1; __utmb=268261020.4.10.1551927447; TawkConnectionTime=0; __uif=__uid%3A8014184671786423146%7C__ui%3A-1%7C__create%3A1551418467; __tb=0; __IP=1786423146',
        'Host': 'cep.com.vn',
        'Referer': 'http://cep.com.vn/news/khoa-hoc-cong-nghe',
        #'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    start_urls = ['http://cep.com.vn/news/']
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     #'Cookie': '_ga=GA1.3.54805363.1551923779; _gid=GA1.3.1366219062.1551923779; __utmc=268261020; __utmz=268261020.1551923779.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); homepage3=visited; __iid=; __su=0; __RC=-1; __R=0; __tawkuuid=e::cep.com.vn::EP2djJgUdS0LLqE8VQMTeyfOckmSlnVjecykSzwVRYag/oU+SBvO0ZENl1sLdw1q::2; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22fe15fa7faad65c17d3bfe3a0bea5ed30%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22106.122.167.106%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A104%3A%22Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F71.0.3578.98+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1551902160%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22site_lang%22%3Bs%3A2%3A%22vi%22%3B%7D23034f0290838dcff32c6cb08d5be7bf; __utma=268261020.54805363.1551923779.1551923779.1551927447.2; __utmt=1; __utmb=268261020.4.10.1551927447; TawkConnectionTime=0; __uif=__uid%3A8014184671786423146%7C__ui%3A-1%7C__create%3A1551418467; __tb=0; __IP=1786423146',
    #     'Host': 'cep.com.vn',
    #     'Referer': 'http://cep.com.vn/news/khoa-hoc-cong-nghe',
    #     #'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # }

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse, dont_filter=True, meta={'tag': 0},)

    def parse(self, response):
        urls = list(set(re.findall('(http://cep.com.vn/news/.*?)"', response.text)))
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            # 'Cookie': '_ga=GA1.3.54805363.1551923779; __utmz=268261020.1551923779.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); homepage3=visited; __iid=; __su=0; __RC=-1; __R=0; __tawkuuid=e::cep.com.vn::EP2djJgUdS0LLqE8VQMTeyfOckmSlnVjecykSzwVRYag/oU+SBvO0ZENl1sLdw1q::2; __tb=0; __utmc=268261020; _gid=GA1.3.1298384420.1552286606; __IP=2015674723; __utma=268261020.54805363.1551923779.1552291894.1552298177.8; __uif=__uid%3A8014184671786423146%7C__ui%3A-1%7C__create%3A1551418467; TawkConnectionTime=0',
            # 'Host': 'cep.com.vn',
            #'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        for url in urls:
            yield Request(url, headers =headers, callback=self.getUrl, meta={'tag': 0}, dont_filter=True)

    def getUrl(self, response):
        urls = response.xpath('//h2[@class="news-title"]/a/@href').extract()
        for url in urls:
            with open('urls.txt', 'r') as f:
                preSaved = f.readlines()
                saved = [x.strip('\n') for x in preSaved]
            with open('urls.txt', 'a') as f:
                if url not in saved:
                    f.write(url + '\n')
        token = response.xpath('//input[@name="cep-token"]/@value').extract_first()
        catId = response.xpath('//div[@class="news-others news-section ajax-news clear-after"]/@data-id').extract_first()
        postsPerpage = response.xpath('//div[@class="news-others news-section ajax-news clear-after"]/@data-num').extract_first()
        offset = response.xpath('//div[@class="news-others news-section ajax-news clear-after"]/@data-offset').extract_first()
        if offset != None:
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                #'Content-Length': '87',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                #'Cookie': '_ga=GA1.3.54805363.1551923779; __utmz=268261020.1551923779.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); homepage3=visited; __iid=; __su=0; __RC=-1; __R=0; __tawkuuid=e::cep.com.vn::EP2djJgUdS0LLqE8VQMTeyfOckmSlnVjecykSzwVRYag/oU+SBvO0ZENl1sLdw1q::2; __tb=0; __utmc=268261020; _gid=GA1.3.1298384420.1552286606; __IP=2015674723; __utma=268261020.54805363.1551923779.1552298177.1552368957.9; __uif=__uid%3A8014184671786423146%7C__ui%3A-1%7C__create%3A1551418467; TawkConnectionTime=0; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e0bfcfdf2dd06d6ae097f46efcb09b33%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22120.36.193.99%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A104%3A%22Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F71.0.3578.98+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1552346747%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22site_lang%22%3Bs%3A2%3A%22vi%22%3B%7D0f867b971de5155fc2dc54562f260457',
                'Host': 'cep.com.vn',
                'Origin': 'http://cep.com.vn',
                'Referer': 'http://cep.com.vn/news/',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            data = {
                'token': token,
                'post_type': 'other_news',
                'cat_id': catId,
                'posts_per_page': postsPerpage,
                'posts_offset': '',
                'data_group': '',
            }
            postsOffset = int(offset) + 1*int(postsPerpage)
            data['posts_offset'] = (str(postsOffset)).zfill(len(str(postsOffset))+1)
            data['data_group'] = '2'
            print(data)
            yield FormRequest(url='http://cep.com.vn/ajax/get_news', callback=self.getUrlnext, formdata=data, headers=headers, meta={'data': data, 'offset': offset, 'postsPerpage': postsPerpage, 'headers': headers, 'tag': 0}, dont_filter=True)

    def getUrlnext(self, response):
        if len(response.text) > 200:
            urls = response.xpath('//h2[@class="news-title"]/a/@href').extract()
            for url in urls:
                with open('urls.txt', 'r') as f:
                    preSaved = f.readlines()
                    saved = [x.strip('\n') for x in preSaved]
                with open('urls.txt', 'a') as f:
                    if url not in saved:
                        f.write(url + '\n')
            data = response.meta['data']
            offset = response.meta['offset']
            postsPerpage = response.meta['postsPerpage']
            data['data_group'] = str(int(data['data_group']) + 1)
            postsOffset = int(offset) + (int(data['data_group'])-1)*int(postsPerpage)
            data['posts_offset'] = (str(postsOffset)).zfill(len(str(postsOffset)) + 1)
            print(data)
            yield FormRequest(url='http://cep.com.vn/ajax/get_news', callback=self.getUrlnext, formdata=data, headers=response.meta['headers'], meta={'data': data, 'offset': offset, 'postsPerpage': postsPerpage, 'headers': response.meta['headers'], 'tag': 0}, dont_filter=True)


