# -*- coding: utf-8 -*-
import scrapy
import csv
import re
import random
from Redfin.items import RedfinItem

class RedfinCrawlerSpider(scrapy.Spider):
    name = 'redfin_crawler'
    allowed_domains = ['redfin.com']

    '''start requests by looping through all valid zipcodes on redfin,
    generate links by zipcode'''
    def start_requests(self):
        with open("all_postal_codes.txt") as f:
            for zipcode in f:
                zipcode = zipcode.rstrip('\n')
                url = 'https://www.redfin.com/zipcode/' + zipcode
                yield scrapy.Request(url=url, callback=self.get_csv_url)

    '''parse and go to download_csv link. Some zipcode may not have it visible,
    use manual link construction can still find it'''
    def get_csv_url(self, response):
        regionId = re.search(r"regionId=(.+?)&",response.text).group(1)
        csv_url = 'https://www.redfin.com/stingray/api/gis-csv?al=1&region_id='+regionId+'&region_type=2&sold_within_days=180&status=9&uipt=1,2,3,4,5,6&v=8'
        return scrapy.Request(url=csv_url,callback=self.parse_csv) 

    '''parse the result csv to item pipeline'''
    def parse_csv(self, response):
        all_items = response.body.decode().split('\n')
        for index, line in enumerate(all_items):      
            if index != 0 and line:
                fields = next(csv.reader(line.splitlines(), skipinitialspace=True))
                item = RedfinItem()
                item['sold_date'] = fields[1]
                item['property_type'] = fields[2]
                item['address'] = fields[3]    
                item['city'] = fields[4]
                item['state'] = fields[5]           
                item['zipcode'] = fields[6]       
                item['price'] = fields[7]     
                item['beds'] = fields[8]
                item['baths'] = fields[9]
                item['square_feet'] = fields[11]
                item['lot_size'] = fields[12]
                item['year_built'] = fields[13]
                item['days_on_market'] = fields[14]
                yield item