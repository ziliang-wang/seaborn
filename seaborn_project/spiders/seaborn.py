import scrapy

from seaborn_project.items import SeabornProjectItem


class SeabornSpider(scrapy.Spider):

    name = 'seaborn'

    def start_requests(self):
        url = 'http://seaborn.pydata.org/examples/index.html'
        yield scrapy.Request(url)

    def parse(self, response):
        data_dict = {}
        divs = response.xpath('//div[@class="figure align-center"]')
        for div in divs:
            data_dict['title'] = div.xpath('.//p/text()').extract_first()
            data_dict['url'] = response.urljoin(div.xpath('./a/@href').extract_first())
            yield scrapy.Request(data_dict['url'],
                                 meta=data_dict,
                                 callback=self.parse_detail)

    def parse_detail(self, response):
        item = SeabornProjectItem()
        item['title'] = response.meta['title']
        item['file_urls'] = [response.urljoin(response.xpath(
            '//a[@class="reference download internal"]/@href').extract_first())]
        yield item




