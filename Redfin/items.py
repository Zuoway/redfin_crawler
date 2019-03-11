# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedfinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sold_date = scrapy.Field()
    property_type = scrapy.Field()
    address = scrapy.Field()         
    city = scrapy.Field()          
    state = scrapy.Field()           
    zipcode = scrapy.Field()             
    price = scrapy.Field()           
    beds = scrapy.Field()            
    baths = scrapy.Field()
    square_feet = scrapy.Field()
    lot_size = scrapy.Field()
    year_built = scrapy.Field()
    days_on_market = scrapy.Field()