import scrapy

class Spider1 (scrapy.Spider):
    name = 'Quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor'
    ]
    def parse(self,response):
        for quote in response.css('div.quote'):
            yield {
                'author' : quote.xpath('span/small/text()').get(),
                'text' : quote.css('span.text::text').get(),
            }
        next_page = response.css('li.next a::attr("herf")').get()
        if next_page is not None:
            yield response.folllow(next_page , self.parse)