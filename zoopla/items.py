# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZooplaItem(scrapy.Item):
    agent = scrapy.Field()
    agent_logo_url = scrapy.Field()
    price = scrapy.Field()
    postcode = scrapy.Field()
    city = scrapy.Field()
