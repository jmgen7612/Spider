# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderdemoItem(scrapy.Item):
    """
    Item 是保存爬取到的数据的容器；其使用方法和python字典类似，
    并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。
    首先根据需要从网站获取到的数据对item进行建模。 我们需要从
    网站中获取名字，url，以及网站的描述。 对此，在item中定义相应的字段
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass
