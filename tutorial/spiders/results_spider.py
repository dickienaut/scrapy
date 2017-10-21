import scrapy
import pickle
import pandas as pd
import pdb

class Rider_Results_Spider(scrapy.Spider):
    name = "results0"

    def __init__(self):
        self.rider_links = pd.read_csv('/Users/diode/Documents/tutorial/tutorial/spiders/Data/rider_links.csv', header=None)[1]
        self.rider_races = []
        self.years = list(range(2008,2018))

    def start_requests(self):
        urls = ['http://www.procyclingstats.com/' + i + '&season=' + str(year) for i in self.rider_links for year in self.years ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.rider_races.append(response)
        print(len(self.rider_races))
        page = response.url.split("/")[-1]
        filename = 'Data/riders_%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)



        # # print(test)
    #     # # print(self.rider_links)
        # # # pdb.set_trace()
        # # page = response.url.split("/")[-2]
        #

        # self.log('Saved file %s' % filename)
        #









#     def parse(self, response):
#         # follow links to author pages
#         for href in response.css('.author + a::attr(href)'):
#             yield response.follow(href, self.parse_author)
#
#         # follow pagination links
#         for href in response.css('li.next a::attr(href)'):
#             yield response.follow(href, self.parse)
#
#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).extract_first().strip()
#
#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # def parse(self, response):
#     #     # pdb.set_trace()
#     #     riders_list = response.xpath('//td[4]/a[1]/@href').extract()
#     #     rider_links.append(riders_list)
#     #     page = response.url.split("/")[-2]
#     #     filename = 'riders-%s.html' % page
#     #     # filename = ''
#     #     # filename = 'riders%s.html' % counter
#     #     # counter += 1
#     #     # print(filename)
#     #     # pdb.set_trace()
#     #     with open(filename, 'wb') as f:
#     #         f.write(response.body)
#     #     self.log('Saved file %s' % filename)
#     #
#     # def parse(self, response):
#     #     # pdb.set_trace()
#     #     riders_list = response.xpath('//td[4]/a[1]/@href').extract()
#     #     rider_links.append(riders_list)
#     #     page = response.url.split("/")[-2]
#     #     filename = 'riders-%s.html' % page
#     #     # filename = ''
#     #     # filename = 'riders%s.html' % counter
#     #     # counter += 1
#     #     # print(filename)
#     #     # pdb.set_trace()
#     #     with open(filename, 'wb') as f:
#     #         f.write(response.body)
#     #     self.log('Saved file %s' % filename)
#
#
#
#
#
#
#
#
#
#
#
# # response.xpath('//tr/td[4]/a[1]')
# # response.xpath('//td[4]/a[1]/@href').extract() good one
