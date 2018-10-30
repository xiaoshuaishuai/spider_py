# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os

from pymongo import MongoClient

from scrapy_leisu_saishi.items import EarthZhouItem, CountryAreaItem, CountryAreaLianSaiItem
from scrapy_leisu_saishi.settings import MONGO_URI, PROJECT_DIR, MONGO_DB, IS_STORE
logger = logging.getLogger('scrapy_leisusaishi_pipeline')

# 爬虫启动时
checkFile = "isRunning.txt"
class ScrapyLeisuSaishiPipeline(object):
    """
    存储数据
    """
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db= None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MONGO_URI,
            mongo_db= MONGO_DB,
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        isFileExsit = os.path.isfile(checkFile)
        if isFileExsit:
            os.remove(checkFile)
        f = open(checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.client.close()
        # 爬虫正常结束时
        isFileExsit = os.path.isfile(checkFile)
        if isFileExsit:
            os.remove(checkFile)

    def process_item(self, item, spider):
        if IS_STORE:
            if isinstance(item,EarthZhouItem):
                self.saveEarthZhouItem(item)
            if isinstance(item, CountryAreaItem):
                self.saveCountryAreaItem(item)
            if isinstance(item, CountryAreaLianSaiItem):
                self.saveCountryAreaLianSaiItem(item)
        return item

    # 保存地球大洲信息
    def saveEarthZhouItem(self, item):
        collection = self.db['earth_zhou']
        earthId = item['id']
        data = collection.find_one({'id':earthId})
        if not data:
            logger.info('保存数据[地球大洲信息] %s',dict(item))
            collection.insert(dict(item))
        else:
            logger.info('数据已存在,data: %s',data)
            collection.update({'id':earthId},dict(item))
        return item
    # 保存国家信息
    def saveCountryAreaItem(self, item):
        collection = self.db['country']
        name = item['name']
        data = collection.find_one({'name': name})
        if not data:
            logger.info('保存数据[国家信息] %s', dict(item))
            collection.insert(dict(item))
        else:
            logger.info('数据已存在, %s',data)
            collection.update({'name': name}, dict(item))
        return item
    # 保存联赛信息
    def saveCountryAreaLianSaiItem(self, item):
        collection = self.db['saishi']
        name = item['id']
        data = collection.find_one({'id': name})
        if not data:
            logger.info('保存数据[联赛] %s', dict(item))
            collection.insert(dict(item))
        else:
            logger.info('数据已存在,%s',data)
            collection.update({'name': name}, dict(item))
        return item