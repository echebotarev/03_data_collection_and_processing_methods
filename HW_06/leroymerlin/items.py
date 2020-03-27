# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from pprint import pprint
from w3lib.html import strip_html5_whitespace
from scrapy.loader.processors import MapCompose, TakeFirst

def filter_photos(href):
    if href.find('w_400,h_400') != -1:
        return href

def prepare_spec(spec):
    output = {}
    output[spec[0]] = strip_html5_whitespace(spec[1])
    return output

def convert_to_int(value):
    return int(value)

class LeroymerlinItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(convert_to_int) ,output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(filter_photos))
    specifications = scrapy.Field(input_processor=MapCompose(prepare_spec))
