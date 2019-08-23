# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

from gitchat.conf.mongo_config import *

class GitchatPipeline(object):
    client = None
    dbname = None
    sheetname = None
    # 可选方法，用于做参数初始化等操作，常用于保存item到文件中穿件文件并打开时用到

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection

        client = pymongo.MongoClient(host=host, port=port)
        self.client = client
        self.dbname = dbname
        self.sheetname = sheetname

    def process_item(self, item, spider):
        data = dict(item)

        sheetname = item.get('sheetname', self.sheetname)
        mydb = self.client[self.dbname]
        self.post = mydb[sheetname]

        self.post.insert(data)
        return item


# 图片管道
class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        #print(item['image_urls'], info)
        for img_item in item['image_urls']:
            #print("@@@@@@@@@@@@@@@要下载的图片是@@@@@@@@@@@@@@@@:"+image_url)
            yield scrapy.Request(img_item['src'], meta={'item': img_item})

    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        #image_name = request.url.split('/')[-1]

        item = request.meta['item']

        image_name = item['tarname'];
        # # 接收上面meta传递过来的图片名称
        # name = request.meta['name']
        # # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        # name = re.sub(r'[？\\*|“<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(item['dirname'], image_name)
        #print("--->", filename, "<----")
        return filename