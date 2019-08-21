#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


class Start():
    def __init__(self):
        self.crawler = CrawlerProcess(get_project_settings())

    def start(self, spider_list):
        for spider in spider_list:
            self.crawler.crawl(spider)
        self.crawler.start()

    def stop(self):
        self.crawler.stop()


def main():
    spider_list = ["phonespider"]
    start = Start()
    start.start(spider_list)


if __name__ == '__main__':
    main()
