import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
    #quote.css('span::text').get() getting the quote text
    #quote.css('small.author::text').get() getting the author
    

