import scrapy
from scrapy_splash import SplashRequest

class WritersSpider(scrapy.Spider):
    name = "writers"
    allowed_domains = ["quotes.toscrape.com"]

    script = '''
      function main(splash, args)
        --splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        --rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
        --rur_tab[5]:mouse_click()
        --assert(splash:wait(1))
        splash:set_viewport_full()
      return {
          --image = splash:png(), -- show a png image of the website
          html = splash:html() -- show the html of the website
        }
      end
              '''
    
    custom_settings = {'ITEM_PIPELINES': {
       'imdb.pipelines.WritersPipeline': 300
    }}

    def start_requests(self):
        yield SplashRequest(url="http://quotes.toscrape.com/js",
                            callback=self.parse,
                            endpoint="execute",
                            args={'lua_source': self.script})

    def parse(self, response):
        
      
        divs = response.xpath('//div[@class="quote"]')


        for i, d in enumerate(divs):
          quote = d.xpath('.//span[@class="text"]/text()').get()
          author = d.xpath('.//small[@class="author"]/text()').get()
          tag_holder = d.xpath('.//div[@class="tags"]')
          tags = tag_holder.xpath('.//a[@class="tag"]/text()').getall()

          yield {'quote': quote,
              'author': author,
              'tags': tags}
          
        
        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page:
            next_page = "http://quotes.toscrape.com" + next_page
            yield SplashRequest(url=next_page,
                            callback=self.parse,
                            endpoint="execute",
                            args={'lua_source': self.script})