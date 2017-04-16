# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Datamining_sample.items import DataminingSampleItem
import csv

class MySpider(BaseSpider):
    name = "uniport"
    allowed_domains = ["uniport.org"]
    start_urls = []
    csvfile1 = open('mt-OGT Parterner Data/jctt1.csv','r')
    csvfile2 = open('mt-OGT Parterner Data/uvrt.csv','r')
    reader1 = csv.DictReader(csvfile1)
    reader2 = csv.DictReader(csvfile2)
    count = 0
    baseUrl = 'http://www.uniprot.org/uniprot/'
    for row in reader1:
        if count < 10000000:
            if len(row['Uniport Accession Number']) != 0:
                url = baseUrl+row['Uniport Accession Number']+'#subcellular_location'
                start_urls.append(url)
            count = count+1
    for row2 in reader2:
        if count < 10000000:
            if len(row2['Accession Number (UNIPROTKB #)']) != 0:
                url = baseUrl+row2['Accession Number (UNIPROTKB #)']+'#subcellular_location'
                start_urls.append(url)
            count = count+1

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        item = DataminingSampleItem()
        item["Name"] = hxs.select('//h1[contains(@property, "schema:name")]/text()').extract()
        item["Accession_Number"] = hxs.select('//strong[contains(@property, "schema:entryID")]/text()').extract()
        item["Subcellular_location"] = hxs.select('//a[contains(@href, "locations")]/text()').extract()
        item["Subcellular_location"].pop()
        if item["Name"] == None:
            item["Name"] = "Not Found"
        if item["Accession_Number"] == None:
            item["Accession_Number"] = "Not Found"
        if len(item["Subcellular_location"]) == 0:
            item["Subcellular_location"] = hxs.xpath('//*[@id="subcellular_location"]/ul/li/a/text()').extract()
            if len(item["Subcellular_location"]) == 0:
                item["Subcellular_location"].append("Not Found")
        if len(item["Accession_Number"]) != 0:
            items.append(item)
        return items


