# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AudiblescrapingItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_narrator = scrapy.Field()
    book_price = scrapy.Field()
    book_imagelink = scrapy.Field()
