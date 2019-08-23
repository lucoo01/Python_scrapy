# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GitchatItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    columnDesc = scrapy.Field()  # 内容
    salenum = scrapy.Field()  # 售卖联

    lessonnum = scrapy.Field()  # 课时
    descContainer = scrapy.Field()  # 课时

    price = scrapy.Field()  # 价格
    catalogview = scrapy.Field()  # 列表
    imgurl = scrapy.Field()  # 列表

    sheetname = scrapy.Field()  # 要存储的表格


    scrapy_url = scrapy.Field()  # 采集的地址来源

    pass
