import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            yield{
                'text': quote.css('span::text').get(),
                'author': quote.css('small.author::text').get(),
                'tag_list': quote.css('div.tags a.tag::text').getall(),
                'quote_href': quote.css('span a').attrib['href']
            }
            relative_author_url = quote.css('span a').attrib['href']
            author_url =
            yield scrapy.Request()

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            next_page_url = 'http://quotes.toscrape.com/' + next_page
            yield response.follow(next_page_url, callback=self.parse)
        pass

    def parse_quote_author(self, response):
        ### scraping the information about the author ###





