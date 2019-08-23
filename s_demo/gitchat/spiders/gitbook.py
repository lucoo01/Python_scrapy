# -*- coding: utf-8 -*-
import scrapy

# from gitchat.items import *
# from gitchat.conf.mongo_config import *
import re
#import pymongo

class GitbookSpider(scrapy.Spider):
    name = 'gitbook'
    allowed_domains = ['gitbook.cn']
    start_urls = ['http://gitbook.cn/']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
    }

    
    result = ['5b30789393f14818da76bdbc']
    def start_requests(self):
    
        urls = []
        for item in self.result:

            url = 'https://gitbook.cn/gitchat/column/'+item
            urls.append(url)
        
        for key, url in enumerate(urls):
            headers = {}
            if key - 1 >= 0:
                headers = {'referer': urls[key-1]}

            yield scrapy.Request(url=url, headers=headers, callback=self.parse)


    def parse(self, response):

        litem = {}

        leftbox = response.css(".columnDetail")

        title = leftbox.css(".columnTitle::text").extract_first()

        if title is None:
            title = response.css("title::text").extract_first()

        author = leftbox.css(".titleInfo a::text").extract_first()
        salenum = leftbox.css(".subscriptionNum .text::text").extract_first()
        lessonnum = leftbox.css(".topicTotalNum .text::text").extract_first()
        imgurl = leftbox.css(".topWrapper img::attr(src)").extract_first()

        columnDesc = leftbox.css(".columnDesc").extract()
        descContainer = leftbox.css(".descContainer").extract()

        rightbox = response.css("#indexRight")

        price = rightbox.css(".catalog_buy_btn_2::text").extract_first()
        price = price.replace('立即购买', '')

        catalogview = rightbox.css(
            ".catalog_view a .catalog_item_content::text").extract()

        litem['title'] = title
        litem['author'] = author
        litem['salenum'] = salenum
        litem['lessonnum'] = lessonnum
        litem['price'] = price
        litem['scrapy_url'] = response.url
        litem['imgurl'] = imgurl

        litem['catalogview'] = catalogview

        litem['descContainer'] = descContainer
        litem['columnDesc'] = columnDesc
        litem['sheetname'] = 'lessoninfo'

        yield litem

        

        pass
