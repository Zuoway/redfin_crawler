# -*- coding: utf-8 -*-

'''Can use pymysql client to upload item directly to MySQL DB.
Or simply take stored json file into mysql within mysql shell
As a proof of concept project, not implemented yet.

For coding challenge purposes, currently exporting file into .csv format
'''

# from scrapy.exporters import JsonItemExporter
from scrapy.exporters import CsvItemExporter

class RedfinPipeline(object):
    # def __init__(self):
    #     self.file = open('data.json', 'wb')
    #     self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
    #     self.exporter.start_exporting()

    # def close_spider(self, spider):
    #     self.exporter.finish_exporting()
    #     self.file.close()

    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item

    def __init__(self):
        #Write csv to Result folder
        self.file = open("Result/redfin_zhuowei.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item