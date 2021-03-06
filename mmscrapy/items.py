# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmScrapyItem(scrapy.Item):
    title = scrapy.Field()
    ean = scrapy.Field()
    description = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
