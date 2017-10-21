import scrapy


class RiderSpider(scrapy.Spider):
    name = "riders"

    def start_requests(self):
        urls = ['http://www.procyclingstats.com/rankings.php?id=10643&id=10643&nation=&team=&page=' + str(i) for i in range (0,28)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'Data/riders_%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)



# len(response.xpath('//tr/td[4]/a[1]'))

# s = R
