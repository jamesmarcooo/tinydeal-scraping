import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]
    start_urls = ["http://web.archive.org/"]

    def parse(self, response):
        pass
