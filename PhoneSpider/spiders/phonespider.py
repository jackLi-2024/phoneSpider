# -*- coding: utf-8 -*-
import json

import requests
import scrapy

ES_HOST = "192.168.1.2"
ES_PORT = "9200"


class PhonespiderSpider(scrapy.Spider):
    name = 'phonespider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://opendata.baidu.com/api.php?resource_name=guishudi&query=18404983792']

    def start_requests(self):
        while True:
            n1 = 1
            for n2 in range(3, 9):
                for n3 in range(10):
                    for n4 in range(10):
                        for n5 in range(10):
                            for n6 in range(10):
                                for n7 in range(10):
                                    for n8 in range(10):
                                        for n9 in range(10):
                                            for n10 in range(10):
                                                for n11 in range(10):
                                                    phoneNum = ""
                                                    for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
                                                        phoneNum += str(n)
                                                    if not phoneNum:
                                                        continue
                                                    url = "http://opendata.baidu.com/api.php?resource_name=guishudi&query=%s" % phoneNum
                                                    yield scrapy.Request(url=url)

    def parse(self, response):
        if not json.loads(response.text).get("data"):
            return
        data = json.loads(response.text).get("data")[0]
        phone = data.get("phoneno")
        city = data.get("city")
        province = data.get("prov")
        es_url = "http://" + ES_HOST + ":" + ES_PORT + "/phone/_update/%s" % str(phone)
        body = {
            "doc": {
                "phone": phone,
                "city": city,
                "province": province
            },
            "detect_noop": False,
            "doc_as_upsert": True
        }
        response = requests.post(es_url, json=body).text
        # print(response)
        # print(body)
