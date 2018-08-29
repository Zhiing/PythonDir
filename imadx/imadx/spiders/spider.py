from scrapy import Spider, Request


class ImadxSpider(Spider):
    name = 'imadx'

    def __init__(self):
        self.index_url = 'https://blog.imadx.com/archives'
        self.base_url = 'https://blog.imadx.com'

    def start_requests(self):
        yield Request(self.index_url, callback=self.parse_index)

    def parse_index(self, response):
        page_url_list = response.xpath('//a[@class="post-title"]/@href').extract()

        yield Request(response.url, callback=self.parse_index, dont_filter=True)

        for page_url in page_url_list:
            yield Request(self.base_url + page_url, callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        url_list = response.xpath('//a/@href').extract()
        yield Request(response.url, callback=self.parse_page, dont_filter=True)

        for url in url_list:
            if str(url)[:1] == '/':
                yield Request(self.base_url + url, callback=self.parse_url, dont_filter=True)

    def parse_url(self, response):
        yield Request(response.url, callback=self.parse_page, dont_filter=True)
