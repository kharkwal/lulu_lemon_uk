# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class UrlItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_link = scrapy.Field()

class LululemonProductDetailsItem(scrapy.Item):
    # define the fields for your item here like:
    avilablity = scrapy.Field()
    product_name = scrapy.Field()
    product_color = scrapy.Field()
    product_size = scrapy.Field()
    mrp_price = scrapy.Field()
    discounted_price = scrapy.Field()
    product_url = scrapy.Field()
    timestamp = scrapy.Field()