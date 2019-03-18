# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import scrapy
import re
class NewsSpider(scrapy.Spider):
    name = 'detail'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        #'Cookie': '_ga=GA1.3.54805363.1551923779; _gid=GA1.3.1366219062.1551923779; __utmc=268261020; __utmz=268261020.1551923779.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); homepage3=visited; __iid=; __su=0; __RC=-1; __R=0; __tawkuuid=e::cep.com.vn::EP2djJgUdS0LLqE8VQMTeyfOckmSlnVjecykSzwVRYag/oU+SBvO0ZENl1sLdw1q::2; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22fe15fa7faad65c17d3bfe3a0bea5ed30%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22106.122.167.106%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A104%3A%22Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F71.0.3578.98+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1551902160%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22site_lang%22%3Bs%3A2%3A%22vi%22%3B%7D23034f0290838dcff32c6cb08d5be7bf; __utma=268261020.54805363.1551923779.1551923779.1551927447.2; __utmt=1; __utmb=268261020.4.10.1551927447; TawkConnectionTime=0; __uif=__uid%3A8014184671786423146%7C__ui%3A-1%7C__create%3A1551418467; __tb=0; __IP=1786423146',
        # 'Host': 'cep.com.vn',
        'Referer': 'http://cep.com.vn/news/khoa-hoc-cong-nghe',
        #'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    with open('/home/xiyujing/cep/urls.txt', 'r') as f:
        start_urls = list(set([x.strip('\n') for x in f.readlines()]))

    def start_requests(self):
        for url in self.start_urls:
            with open('saved.txt', 'r') as p:
                savedUrls = [x.strip('\n') for x in p.readlines()]

                if url not in savedUrls:
                    yield Request(url, callback=self.parse, headers=self.headers, meta={'tag': 0, 'detail': True}, dont_filter=True)

    def parse(self, response):
        if response.status == 200:
            title = response.url.split('/')[-1]
            selectorVi = response.xpath('//div[@id="vietnamese"]/p')
            selectorEn = response.xpath('//div[@id="english"]/p')
            sentencesVi = [x.xpath('string(./span)').extract_first() for x in selectorVi]
            sentencesEn = [x.xpath('string(./span)').extract_first() for x in selectorEn]
            with open(f'{title}_vi.txt', 'a') as f:
                for i in sentencesVi:
                    if i.strip() != '':
                        f.write(i.replace('\n', '') + '\n')
            with open(f'{title}_en.txt', 'a') as p:
                for i in sentencesEn:
                    if i.strip() != '':
                        p.write(i.replace('\n', '') + '\n')


