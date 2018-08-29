# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import urlencode
import time, requests, json


class WeiboSpider(Spider):
    name = 'weibo_index'

    def __init__(self):
        # 读取 关键词
        with open('key_words.txt', encoding='utf-8') as kw_file:
            self.word_list = str(kw_file.read()).split('\n')  # 获取关键词列表
            # sdate=2016-05-23&edate=2018-05-22
        self.sdate = '2016-05-23'  # 开始时间
        self.edate = '2018-05-22'  # 结束时间
        

    def start_requests(self):
        # 构造请求 获得参数
        for word_item in self.word_list:
            time_now = str(time.time()).replace('.', '')[:13]  # 当前时间
            req_data = {  # 请求参数
                'word': word_item,
                'flag': 'nolike',
                '_t': '0',
                '__rnd': time_now
            }
            queries = urlencode(req_data)
            url = 'http://data.weibo.com/index/ajax/hotword?' + queries
            meta = {
                'meta_rnd': time_now
            }
            yield Request(url, callback=self.parse_cookie, meta=meta)


    def parse_cookie(self, response):
        # 获得cookie 并提交服务器 验证
        response_dict = json.loads(response.body_as_unicode())
        # response_dict = {"code":"100000","msg":"\u64cd\u4f5c\u6210\u529f","data":{"id":"1061301160000066618","word":"iphone5s","is_real":"1"}}
        if response_dict['code'] == "100000":
            wid = response_dict['data']['id']
            wname = response_dict['data']['word']
            # ... 
            #  get cookies ...
            # http://data.weibo.com/index/hotword?
            # wid=1030000000269&wname=iphone
            req_data = {
                'wid': wid,
                'wname': wname
            }
            queries = urlencode(req_data)
            url = 'http://data.weibo.com/index/hotword?' + queries
            # ---- #
            headers = {
                'Referer': 'http://data.weibo.com/index',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }
            try:
                req_res = requests.get(url, headers=headers)
                cookies = req_res.cookies.get_dict()
            except:
                print('>>> 获取 cookies 失败! 请终止并调试 <<<')
            # cookies = {'PHPSESSID': 'erqnu8pe3o17b8ei4o1gq381h5', 'WEB3': 'b2b0f7b82c73f523535a8b5a316def6c'}
            # ---- #
            # ...
            # http://data.weibo.com/index/ajax/getchartdata?
            # wid=1061301160000066618&sdate=2018-05-01&edate=2018-05-21&__rnd=1526980448823
            data_dict = {
                'wid': req_data['wid'],
                'sdate': self.sdate,
                'edate': self.edate,
                '__rnd': response.meta['meta_rnd']
            }
            queries = urlencode(data_dict)
            data_url = 'http://data.weibo.com/index/ajax/getchartdata?' + queries
            yield Request(data_url, callback=self.parse_index, cookies=cookies, meta=req_data)
        else:
            print(response_dict)
            # print(response.text)
            print('错误信息...')
            

    def parse_index(self, response):
        response_dict = json.loads(response.body_as_unicode())
        # print(response_dict)
        # 解析 json dict
        yd = response_dict['yd']
        for day in yd:
            # day = {'daykey': '2018-05-17', 'pc': '895', 'mobile': '15700'}
            item = {
                'wid': response.meta['wid'],
                'wname': response.meta['wname'],
                'daykey': day['daykey'],
                'mobile': day['mobile'],
                'pc': day['pc']
            }
            # print(item)
            yield item

