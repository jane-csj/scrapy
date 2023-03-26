import scrapy


class StocksSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["https://gushitong.baidu.com/blocklist/ab-HY"]
    start_urls = ["https://gushitong.baidu.com/blocklist/ab-HY"]


    def parse(self, response):
        print(response.text)
