# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, Compose

def process_image(value):
    value = value[0].split(',')[-1].split()[0]

    return value


class ImgDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    image = scrapy.Field(input_processor=Compose(process_image), output_processor=TakeFirst())
    _id = scrapy.Field()
