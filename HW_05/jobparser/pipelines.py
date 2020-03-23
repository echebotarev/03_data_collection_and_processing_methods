# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from jobparser.get_digits import get_digits

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.vacansy

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]

        item['salary_min'] = get_salary(item['salary'], spider.name, 'min')
        item['salary_max'] = get_salary(item['salary'], spider.name, 'max')

        item['jobsmaker'] = spider.name

        collection.insert_one(item)
        return item

def get_salary(salary, site, priceType):
    if site == 'sjru':
        if len(salary) == 1 or len(salary) == 0:
            return None
        elif len(salary) == 3:
            if priceType == 'min':
                return get_digits(salary[0])
            elif priceType == 'max':
                return get_digits(salary[1])
        elif len(salary) == 4:
            return get_digits(salary[2])

    elif site == 'hhru':
        if len(salary) == 1 or len(salary) == 0:
            return None
        elif len(salary) == 5:
            return get_digits(salary[1])
        elif len(salary) == 6 or len(salary) == 7:
            if priceType == 'min':
                return get_digits(salary[1])
            elif priceType == 'max':
                return get_digits(salary[3])
