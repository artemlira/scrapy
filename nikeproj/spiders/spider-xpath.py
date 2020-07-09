import scrapy


class ScrapeSpider(scrapy.Spider):
    name = 'my_scraper'
    start_urls = ['https://www.nike.com/']

    def parse(self, responce):
        for shoes in responce.xpath('//div[@class="d-lg-b"]'):
            yield {
                'type': shoes.xpath('./a[@class="product-card__link-overlay"]/text()').extract_first(),
                'price': shoes.xpath('./div[@class="product-price css-11s12ax is--current-price"]/text()').extract_first()
            }
