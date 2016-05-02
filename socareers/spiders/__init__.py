import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule

from socareers.items import JobItem

class SOSpider(scrapy.Spider):
    name="socareers"
    allowed_domains = ["careers.stackoverflow.com","stackoverflow.com"]

    start_urls = [
        "http://careers.stackoverflow.com/jobs?searchTerm=&type=&location=&range=20&distanceUnits=Km",
    ]
    job_ids = set()


    def parse(self, response):
        for sel in response.xpath('//div[@data-jobid]'):
            id =''.join(sel.xpath('@data-jobid').extract())
            item = None
            if id not in self.job_ids:
                item = JobItem()
                item['_id'] = id
                item['title'] = ''.join(sel.xpath('div/h1/a/text()').extract())
                item['salary'] = ''.join(sel.xpath('div/span/text()').extract()).strip()
                item['company'] = ''.join(sel.xpath('ul/li[@class="employer"]/text()').extract()).strip()
                item['location'] = ''.join(sel.xpath('ul/li[@class="location"]/text()').extract()).strip()
                item['remote'] = ''.join(sel.xpath('ul/li[@class="remote"]/text()').extract()).strip()
                item['tags'] = sel.xpath('div[@class="tags"]/p/a/text()').extract()
            else:
                print "duplicate"

            yield item
        next_page = response.css("div.pagination > a.test-pagination-next::attr('href')").extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, self.parse)