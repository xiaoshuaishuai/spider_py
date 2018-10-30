# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLeisuSaishiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 地球赛事大洲划分
class EarthZhouItem(scrapy.Item):
    # 1 欧洲
    # 2 非洲
    # 3 亚洲
    # 4 大洋洲
    # 5 北美洲
    # 6 南美洲
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()


# 国家地区
class CountryAreaItem(scrapy.Item):
    # 国家或地区编号
    code = scrapy.Field()
    name = scrapy.Field()
    logo_name = scrapy.Field()
    logo_path = scrapy.Field()
    earthId = scrapy.Field()


# 国家地区联赛
class CountryAreaLianSaiItem(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    type = scrapy.Field()
    level = scrapy.Field()
    description = scrapy.Field()
    categoryId = scrapy.Field()
    uniqueTournamentId = scrapy.Field()
    name_en = scrapy.Field()
    name_zht = scrapy.Field()
    color = scrapy.Field()
    name_id = scrapy.Field()
    name_ja = scrapy.Field()
    name_ko = scrapy.Field()
    name_th = scrapy.Field()
    name_vi = scrapy.Field()
    shortname = scrapy.Field()
    countryCode = scrapy.Field()
    ishot = scrapy.Field()
    shortname_en = scrapy.Field()
    shortname_zht = scrapy.Field()
    continentCode = scrapy.Field()
