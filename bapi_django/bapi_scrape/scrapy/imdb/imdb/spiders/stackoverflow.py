import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from bapi_scrape.scrapy.imdb.imdb.items import ImdbItem

from scrapy.shell import inspect_response

import time
from time import strftime

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['www.stackoverflow.com', 'stackoverflow.com']
    count = 0

    today = strftime('%Y-%m-%d')

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

    custom_settings = {'ITEM_PIPELINES': {
       'imdb.pipelines.StackOverflowPipeline': 300
    }}

    def start_requests(self):
        yield scrapy.Request(url="https://stackoverflow.com/tags?tab=name",
                            headers={'User-Agent': self.user_agent})

    def parse(self, response):
        
      
        tags = response.xpath("//a[@class='post-tag']")
        questions = response.xpath("//div[@class='mt-auto d-flex jc-space-between fs-caption fc-black-400']/div[@class='flex--item']")

        #//div[@class='mt-auto d-flex jc-space-between fs-caption fc-black-400']/div/text()

        #inspect_response(response, self)

        #"147 questions"

        # int(q.split(" ")[0])

        for t, q in zip(tags, questions):
            yield {'date': self.today,
                   'tag': t.xpath('./text()').get(),
                   'questions': int(q.xpath('./text()').get().split(" ")[0]),
                   }
        
        next_page = response.xpath("//a[@class='s-pagination--item js-pagination-item' and @rel='next']/@href").get()

        self.count += 1

        if next_page and self.count < 6:
            next_page = "https://stackoverflow.com"+ next_page
            
            yield scrapy.Request(url=next_page,
                            callback=self.parse)