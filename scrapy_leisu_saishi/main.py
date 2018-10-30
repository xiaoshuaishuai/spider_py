from scrapy import cmdline
# https://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/jobs.html
# cmdline.execute('scrapy crawl leisu_saishi_spider  -s JOBDIR=crawls/somespider-1'.split())
cmdline.execute('scrapy crawl leisu_saishi_spider'.split())