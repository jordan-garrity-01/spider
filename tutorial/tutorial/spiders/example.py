# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['https://velotio.com']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in response.selector.xpath("//body//text()").extract())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        print(text.encode('utf-8'))
        self.logger.info(text)