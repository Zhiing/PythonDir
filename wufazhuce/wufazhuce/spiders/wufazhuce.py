from scrapy import Spider, Request


class WufazhuceSpider(Spider):
    name = 'wufazhuce'

    def __init__(self):
        pass

    def start_requests(self):
        yield Request('http://wufazhuce.com/', callback=self.parse_index)

    def parse_index(self, response):
        photo_max_url = response.xpath('//div[@class="item active"]/a/@href').extract_first()
        article_max_url = response.xpath('//p[@class="one-articulo-titulo"]/a/@href').extract_first()
        question_max_url = response.xpath('//p[@class="one-cuestion-titulo"]/a/@href').extract_first()

        self.photo_list = int(photo_max_url.split('/')[-1])
        self.article_list = int(article_max_url.split('/')[-1])
        self.question_list = int(question_max_url.split('/')[-1])

        for photo_id in range(1, self.photo_list):
            meta = {'photo_id': photo_id}
            photo_url = 'http://wufazhuce.com/one/{0}'.format(photo_id)
            yield Request(photo_url, callback=self.parse_photo, meta=meta)

        for article_id in range(1, self.article_list):
            meta = {'article_id': article_id}
            article_url = 'http://wufazhuce.com/article/{0}'.format(article_id)
            yield Request(article_url, callback=self.parse_article, meta=meta)

        for question_id in range(1, self.question_list):
            meta = {'question_id': question_id}
            question_url = 'http://wufazhuce.com/question/{0}'.format(question_id)
            yield Request(question_url, callback=self.parse_question, meta=meta)

    def parse_photo(self, response):
        dom = response.xpath('//p[@class="dom"]/text()').extract_first()
        may = response.xpath('//p[@class="may"]/text()').extract_first()
        item = {
            'photo_id': response.meta.get('photo_id'),
            'photo_url': response.xpath('//div[@class="one-imagen"]/img/@src').extract_first().replace('"', '').replace(';', ''),
            'photo_date': dom + ' ' + may,
            'photo_text': response.xpath('//div[@class="one-cita"]/text()').extract_first().replace('"', '').replace(';', ''),
            'wufazhuce_url': response.url
        }

        yield item

    def parse_article(self, response):
        item = {
            'article_id': response.meta.get('article_id'),
            'article_title': response.xpath('//h2[@class="articulo-titulo"]/text()').extract_first().replace('"', '').replace(';', ''),
            'article_author': response.xpath('//p[@class="articulo-autor"]/text()').extract_first().replace('"', '').replace(';', ''),
            'article_text': response.xpath('//div[@class="comilla-cerrar"]/text()').extract_first().replace('"', '').replace(';', ''),
            'article_body': str(response.xpath('//*[@id="main-container"]/div/div/div/div/div[2]//text()').extract()).replace('"', '').replace(';', ''),
        }
        yield item

    def parse_question(self, response):
        item = {
            'question_id': response.meta.get('question_id'),
            'question_title': response.xpath('//div[@class="one-cuestion"]/h4[1]/text()').extract_first().replace('"', '').replace(';', ''),
            'question_text': response.xpath('//*[@id="main-container"]/div/div/div/div/div[2]/text()').extract_first().replace('"', '').replace(';', ''),
            'question_body': str(response.xpath('//*[@id="main-container"]/div/div/div/div/div[4]//text()').extract()).replace('"', '').replace(';', '')
        }
        yield item
