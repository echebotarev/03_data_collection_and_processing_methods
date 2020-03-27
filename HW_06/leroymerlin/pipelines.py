# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pprint import pprint
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class LeroymerlinPipeline(object):
    def process_item(self, item, spider):
        pprint(item)
        return item

class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)


    def item_completed(self, results, item, info):
        if results:
           item['photos'] = [itm[1] for itm in results if itm[0]]
        return item