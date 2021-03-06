# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_leisu_saishi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'scrapy_leisu_saishi'

SPIDER_MODULES = ['scrapy_leisu_saishi.spiders']
NEWSPIDER_MODULE = 'scrapy_leisu_saishi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_leisu_saishi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_leisu_saishi.middlewares.ScrapyLeisuSaishiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_leisu_saishi.middlewares.ScrapyLeisuSaishiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_leisu_saishi.pipelines.ScrapyLeisuSaishiPipeline': 300,
   # 引入Scrapy提供的ImagesPipeline组件
   # 'scrapy.pipelines.images.ImagesPipeline': 400,
}
# ImagesPipeline辅助配置项
# 图片存储路径(绝对路径 or 相对路径)
IMAGES_STORE = 'D:\\shuaishuai\\work\\pythonProject\\files\\scrapy\\leisu\\'
# 该字段的值为XxxItem中定义的存储图片链接的image_urls字段
# IMAGES_URLS_FIELD='logo_path'
# # 该字段的值为XxxItem中定义的存储图片信息的logo_path字段
# IMAGES_RESULT_FIELD='logo_name'
# 生成缩略图(可选)
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270),
# }
# 过期时间,单位:天(可选)
IMAGES_EXPIRES = 120
# 过滤小图片(可选)
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
# 是否允许重定向(可选)
# MEDIA_ALLOW_REDIRECTS = True
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# 项目路径
PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.curdir))
# mongodb配置
MONGO_URI = 'mongodb://192.168.225.1:27017'
MONGO_DB = 'py'
IS_STORE = True