import sched
import os

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
import subprocess
import time
from scrapy import cmdline
schedule = sched.scheduler(time.time, time.sleep)
from subprocess import Popen

# 被周期性调度触发的函数
def func():
    subprocess.Popen('scrapy crawl leisu_saishi_spider'.split())
    # os.system("scrapy crawl leisu_saishi_spider --nolog")
    # subprocess.Popen("scrapy crawl leisu_saishi_spider --nolog")
    # cmdline.execute('scrapy crawl leisu_saishi_spider'.split())
def perform1(inc):
    schedule.enter(inc, 0, perform1, (inc,))
    func()  # 需要周期执行的函数


def mymain():
    # 每隔一天运行一次 24*60*60=86400s
    schedule.enter(0, 0, perform1, (120,))


if __name__ == '__main__':
    print('调度函数运行==============')
    mymain()
    schedule.run()
