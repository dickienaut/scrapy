import scrapy
import pickle
import pandas as pd
import pdb

class Rider_Results_Spider(scrapy.Spider):
    name = "local_results"
    allowed_domains = []
    start_urls = ['file:///Users/diode/Documents/tutorial/tutorial/spiders/Data/riders_Adam_Yates&season=2016.html']

    def __init__(self):


    def start_requests(self):
        urls = ['http://www.procyclingstats.com/' + i + '&season=' + str(year) for i in self.rider_links for year in self.years ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
