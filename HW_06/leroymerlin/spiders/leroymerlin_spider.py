# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from leroymerlin.items import LeroymerlinItem

class LeroymerlinSpiderSpider(scrapy.Spider):
    name = 'leroymerlin_spider'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/catalogue/listovye-materialy/']

    def parse(self, response:HtmlResponse):
        links = response.xpath("//div[contains(@class, 'section-card__items')]//li/a/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.parse_catalogs)

    def parse_catalogs(self, response:HtmlResponse):
        links = response.xpath("//div[@class='product-name']/a[contains(@class, 'product-name-inner')]/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response:HtmlResponse):
        loader = ItemLoader(item=LeroymerlinItem(), response=response)
        loader.add_xpath("name", "//h1/text()")
        loader.add_xpath("photos", "//picture[@slot='pictures']/source/@srcset")
        loader.add_xpath("price", "//uc-pdp-price-view[@slot='primary-price']/span[@slot='price']/text()")

        keys = loader.get_xpath("//div[@class='def-list__group']/dt[@class='def-list__term']/text()")
        values = loader.get_xpath("//div[@class='def-list__group']/dd[@class='def-list__definition']/text()")

        loader.add_value("specifications", zip(keys, values))
        yield loader.load_item()


