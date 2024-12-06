# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from numpy.ma.core import append
from pymongo import MongoClient
import re


class JobparserPipeline:
    def __init__(self):
        client = MongoClient({'localhost': 27017})
        self.mongo_base = client.vacancies_novosib_v2

    def process_item(self, item, spider):
        if item['salary']:
            item['salary'] = map(lambda x: re.sub(r'\xa0', '', x), item['salary'])
            item['salary'] = map(lambda x: re.sub(r'\от ', 'min', x), item['salary'])
            item['salary'] = map(lambda x: re.sub(r'\ до |до ', 'max', x), item['salary'])
            item['salary'] = filter(lambda x: re.fullmatch(r'min|max|\d+|[$,₽]', x), item['salary'])
            item['salary'] = list(map(lambda x: int(x) if x.isdigit() else x, item['salary']))

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        return item