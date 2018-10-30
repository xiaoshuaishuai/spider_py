# -*- coding: utf-8 -*-
import json

import scrapy
import logging
import re
import os
from scrapy import Selector, Request, FormRequest

from scrapy_leisu_saishi.items import EarthZhouItem, CountryAreaItem, CountryAreaLianSaiItem
from scrapy_leisu_saishi.settings import IMAGES_STORE

logger = logging.getLogger('leisu_saishi_spider')


class Leisu_Saishi_Spider(scrapy.Spider):

    name = 'leisu_saishi_spider'
    allowed_domains = ['leidata.com']
    # 1 欧洲
    # 2 非洲
    # 3 亚洲
    # 4 大洋洲
    # 5 北美洲
    # 6 南美洲
    start_urls = ['http://www.leidata.com/zh/database/category']
    start_urls_2 = 'http://www.leidata.com/zh/database/'
    array = []
    showCountryCodeChild = 'showCountryCodeChild'

    def start_requests(self):
        return [Request(
            self.start_urls[0],
            callback=self.post_category
        )]

    def post_category(self, response):
        slt = Selector(response)
        zhou = slt.xpath('//p[@class="football_date_tab"]')
        for index, d in enumerate(zhou.xpath('a').extract()):
            if 0 != index:
                earthItem = EarthZhouItem()
                earthItem['id'] = str(index)
                earthItem['name'] = zhou.xpath('a[' + str(int(index + 1)) + ']/text()').extract()
                half_url = str(zhou.xpath('a[' + str(int(index + 1)) + ']/@href').extract())
                # logger.info('halfurl，%s',half_url)
                # url = self.start_urls[0]+'?'+half_url.split('?')[1]
                # logger.info("====as=da=sd=as=d=as %s",self.start_urls_2+half_url[2:-2])
                earthItem['url'] = self.start_urls_2 + half_url[2:-2]
                self.array.append(earthItem)
                yield earthItem
        for s in self.array:
            # logger.info('肉丝胖死 %s',s.get('url'))
            yield Request(
                s.get('url'),
                callback=self.parse_get_counrty, dont_filter=True
            )
        # self.parse_get_saishi(slt)

    # 获取国家信息
    def parse_get_counrty(self, response):
        slt = Selector(response)
        # 各大洲的id值
        earthId = response.url[-1]
        ul = slt.xpath('//div[@id="menu"]/ul')
        # logger.info(ul)
        pattern = re.compile("'(.*)'")
        for county in ul:
            countryAreaItemNames = county.xpath('li[@class="team_list"]/a/span/text()').extract()
            # countryCodeChild = county.xpath('li[@class="team_list"]/a/@onmouseover').extract()
            # for countryCodeChildHtml in countryCodeChild:
            #     # ["showCountryCodeChild('102',this)", "showCountryCodeChild('101',this)", "showCountryCodeChild('106',this)", "showCountryCodeChild('103',this)", "showCountryCodeChild('105',this)", "showCountryCodeChild('107',this)", "showCountryCodeChild('104',this)", "showContinetChild('1',this)", "showContinetChild('2',this)", "showContinetChild('3',this)", "showContinetChild('4',this)", "showContinetChild('5',this)", "showContinetChild('6',this)", "showContinetChild('7',this)"]
            #     if countryCodeChildHtml.startswith('showCountryCodeChild'):
            #         # logger.info('countryCodeChildHtml %s', countryCodeChildHtml)
            #         countryAndAreaCodes = pattern.findall(countryCodeChildHtml)
            #         logger.info('countryAndAreaCodes: %s', countryAndAreaCodes[0])
            #     #     for countryCode in countryAndAreaCodes:
            #     #         logger.info('countryCode%s', countryCode)

            # countrySaishiNames = county.xpath('li[@class="team_list"]/ul/li/a/span/text()').extract()
            # logger.info('countrySaishiNames %s', countrySaishiNames)
            # TODO 解析image
            # logoUrls = county.xpath('li[@class="team_list"]')

            # if('欧洲' == countryName):
            #     break
            # logger.info("logoUrls %s",logoUrls.xpath('style'))
            # logger.info('countryNames',countryNames)
            for index, countryName in enumerate(countryAreaItemNames):
                if '欧洲' == countryName or '非洲' == countryName or '亚洲' == countryName or '大洋洲' == countryName or '北美洲' == countryName or '南美洲' == countryName or '世界' == countryName:
                    continue
                countryAreaItem = CountryAreaItem()
                # countryAndHongkongItem['id'] = str(int(index + 1))
                countryCodeChildHtml = county.xpath('li[@class="team_list"]/a/@onmouseover').extract()[index]
                if countryCodeChildHtml.startswith('showCountryCodeChild'):
                    # logger.info('countryCodeChildHtml %s', countryCodeChildHtml)
                    countryAndAreaCodes = pattern.findall(countryCodeChildHtml)
                    # logger.info('countryAndAreaCodes: %s', countryAndAreaCodes[0])
                    countryAreaItem['code'] = countryAndAreaCodes[0]
                    logoName = str(countryAndAreaCodes[0])+'.jpg'
                    countryAreaItem['logo_path'] = 'http://www.leidata.com/images/soccer/logo/category/'+logoName
                    countryAreaItem['logo_name'] = logoName
                    yield Request(countryAreaItem['logo_path'],callback=self.parse_logo)
                    # self.post_saishi(countryAndAreaCodes[0])
                    yield FormRequest(
                        'http://www.leidata.com/zh/database/uniqueTournament_ajax',
                        method='POST',
                        formdata={
                            'countryCode': countryAndAreaCodes[0]}, callback=self.parse_liansai, dont_filter=True
                    )

                countryAreaItem['name'] = countryName
                countryAreaItem['earthId'] = earthId
                yield countryAreaItem

    def parse_logo(self, response):
        logger.info('处理图片信息:%s',response.url)
        url = str(response.url)
        imgName= url[int(url.rfind('/'))+1:]
        logger.info('imgName %s',imgName)
        fileName = IMAGES_STORE+imgName
        if os.path.exists(fileName) is False:
            logger.info('写入图片文件********************* %s',fileName)
            with open(fileName,'wb') as f:
                f.write(response.body)

    def parse_liansai(self, response):
        # logger.info('解析联赛====== %s', response.body)
        # 处理json格式数据
        js = json.loads(response.body)
        for item in js:
            countryAreaLianSaiItem = CountryAreaLianSaiItem()
            countryAreaLianSaiItem['name'] = item['name']
            countryAreaLianSaiItem['id'] = item['id']
            countryAreaLianSaiItem['type'] = item['type']
            countryAreaLianSaiItem['level'] = item['level']
            countryAreaLianSaiItem['description'] = item['description']
            countryAreaLianSaiItem['categoryId'] = item['categoryId']
            countryAreaLianSaiItem['uniqueTournamentId'] = item['uniqueTournamentId']
            countryAreaLianSaiItem['name_en'] = item['name_en']
            countryAreaLianSaiItem['name_zht'] = item['name_zht']
            countryAreaLianSaiItem['color'] = item['color']
            countryAreaLianSaiItem['name_id'] = item['name_id']
            countryAreaLianSaiItem['name_ja'] = item['name_ja']
            countryAreaLianSaiItem['name_ko'] = item['name_ko']
            countryAreaLianSaiItem['name_th'] = item['name_th']
            countryAreaLianSaiItem['name_vi'] = item['name_vi']
            countryAreaLianSaiItem['shortname'] = item['shortname']
            countryAreaLianSaiItem['countryCode'] = item['countryCode']
            countryAreaLianSaiItem['ishot'] = item['ishot']
            countryAreaLianSaiItem['shortname_en'] = item['shortname_en']
            countryAreaLianSaiItem['shortname_zht'] = item['shortname_zht']
            countryAreaLianSaiItem['continentCode'] = item['continentCode']
            yield countryAreaLianSaiItem

    def parse_err(self, response):
        self.logger.ERROR('爬虫crawl {} failed'.format(response.url))
