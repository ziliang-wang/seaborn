# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline


class SeabornProjectPipeline(object):
    def process_item(self, item, spider):
        return item


class SeabornFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url,
                                 meta={'title': item['title']})

    def item_completed(self, results, item, info):
        file_info = [x['path'] for ok, x in results if ok]
        if not file_info:
            raise DropItem('No such file')
        return item

    def file_path(self, request, response=None, info=None):
        folder_name = request.meta['title']
        file_name = request.url.split('/')[-1]
        return '{}/{}'.format(folder_name, file_name)
