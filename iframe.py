from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy import Request

class Dummy(Item):
    titulo = Field()
    titulo.iframe= Field()

class W3SCrawler (CrawlSpider):
    name = 'w3s'
    custom_settings = {
    'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }

    allowed_domains = ['w3schools.com']
    start_urls = ['https:\\www.w3schools.com/html/html_iframe.asp"]

    download_delay = 2

    def parse(self, response):
        sel = Selector(response)
        titulo = sel.xpath('//div[@id="main]//h1/span/text()