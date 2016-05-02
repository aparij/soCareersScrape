# -*- coding: utf-8 -*-
import scrapy


class JobItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    tags = scrapy.Field()
    location = scrapy.Field()
    remote = scrapy.Field()

