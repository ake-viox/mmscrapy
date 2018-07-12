# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# This pipeline will rename the downloaded image to the scraped ean code

import scrapy
from scrapy.pipelines.images import FilesPipeline
from scrapy.exceptions import DropItem

class SaveImagesPipeline(FilesPipeline): 
    
    def get_media_requests(self, item, info): 
        for image_url in item['file_urls']: 
            filename = item['ean']
            yield scrapy.Request(image_url, meta={'filename': filename}) 
        return 
        
    def file_path(self, request, response=None, info=None): 
        return '%s.jpg' % request.meta.get('filename')

# In case of multiple images rename to ean_1.jpg, ean_2.jpg, ...   
#
#    def get_media_requests(self, item, info): 
#        i = 1 
#        for image_url in item['image_urls']: 
#            filename = '{}_{}.jpg'.format(item['ean'], i) 
#            yield scrapy.Request(image_url, meta={'filename': filename}) 
#            i += 1 
#        return 