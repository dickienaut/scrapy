import scrapy
import pickle
import pandas as pd
import pdb

class Rider_link_Spider(scrapy.Spider):
    name = "riders2"

    def __init__(self):
        self.rider_links = pd.Series()

    def start_requests(self):
        urls = ['http://www.procyclingstats.com/rankings.php?id=10643&id=10643&nation=&team=&page=' + str(i) for i in range(1,28)]
        # urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        print("Success!")
        # pdb.set_trace()
        # finally:
        #     pickle.dump(self.rider_links, open("Data/rider_links.pkl", "wb"))

    def parse(self, response):
        riders_list = response.xpath('//td[4]/a[1]/@href').extract()
        test = pd.Series(riders_list)
        self.rider_links = self.rider_links.append(test)
        save_links = self.rider_links
        save_links.to_csv('Data/rider_links.csv')
        # self.rider_links.to_csv( 'rider_links.csv')
        print(len(self.rider_links))
        # test = self.rider_links
        # test.to_csv('test.csv')
        # for rider in self.rider_links:
        #     print(rider)
        # # for rider in riders_list[0]:
        # #     rider_temp =
        # #     self.rider_links.append(rider)
        # # print(test)
        # # print(self.rider_links)
        # # # pdb.set_trace()
        # # page = response.url.split("/")[-2]
        #
        # filename = 'Data/riders_%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        #








a = 1

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
