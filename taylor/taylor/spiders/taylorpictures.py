# -*- coding: utf-8 -*-
import scrapy


class TaylorpicturesSpider(scrapy.Spider):
    name = 'taylorpictures_01'

    def __init__(self):
        self.post_base_url = 'http://taylorpictures.net/displayimage.php?pid='
        self.post_id_list = [x for x in range(202823, -1, -1)]

    def start_requests(self):
        for i in self.post_id_list:
            post_url = self.post_base_url + str(i)
            yield scrapy.Request(post_url, callback=self.parse_page)

        # test
        # url = 'http://taylorpictures.net/displayimage.php?pid=202823'
        # yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        album_title = response.xpath('//td[@class="tableh1"]/a[last()]/text()').extract_first()
        album_id = response.xpath('//td[@class="tableh1"]/a[last()]/@href').re('album=(\d+)')
        img_url = response.xpath('//img[@class="image"]/@src').extract_first()
        # 参数
        if img_url is not None:
            meta = {
                'album_title': album_title,
                'album_id': album_id[0],
                'img_url': 'http://taylorpictures.net/' + str(img_url).replace('normal_', '')
            }
            yield (meta)
        # yield meta
        # paghe_photo_url = response.url + '&fullsize=1'
        # if album_id is not None:
        #     yield scrapy.Request(paghe_photo_url, callback=self.parse_photo, meta=meta)
        # else:
        #     print('album_id is None', response)

    # def parse_photo(self, response):
    #     try:
    #         item = {
    #             'album_id': response.meta['album_id'],
    #             'album_title': response.meta['album_title'],
    #             'img_url': 'http://taylorpictures.net/' + response.xpath('//img/@src').extract_first()
    #         }
    #         yield item
    #     except Exception as e:
    #         print('what the fuck.', e)
