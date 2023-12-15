import scrapy
from ..items import OrgExampleItem


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['example.org']
    start_urls = ['https://example.org/']

    def parse(self, response):
        title = response.xpath('/html/body/div/h1/text()').extract_first()
        content = response.xpath('/html/body/div/p[1]/text()').extract_first()
        link = response.xpath('/html/body/div/p[2]/a/@href').extract_first()

        item = OrgExampleItem()
        item['title'] = title
        item['content'] = content
        item['link'] = link
        return item
    