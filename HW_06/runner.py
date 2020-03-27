from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leroymerlin.spiders.leroymerlin_spider import LeroymerlinSpiderSpider
from leroymerlin import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpiderSpider)
    process.start()
