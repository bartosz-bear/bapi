import scrapy

class FancyGlasses(scrapy.Spider):
    name = 'fancy_glasses'
    allowed_domains = ['www.glassesshop.com']

    custom_settings = {'ITEM_PIPELINES': {
       'imdb.pipelines.FancyGlassesPipeline': 300
    }}

    def start_requests(self):
      yield scrapy.Request(url='https://www.glassesshop.com/bestsellers',
                           callback=self.parse)

    def parse(self, response):
   
        glasses = response.xpath('//div[@id="product-lists"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]')

        for g in glasses:
          name = g.xpath('.//div[@class="product-img-outer"]/a/@title').get()
          price = g.xpath('.//div[@class="mt-3"]//div[@class="p-price"]/div/span/text()').get()
          product_url = g.xpath('.//div[@class="product-img-outer"]/a/@href').get()
          product_image_url = g.xpath('.//div[1]/div[1]/div/span/@data-try-it-on').get()

          yield {'name': name,
                'price': float(price.replace('$', '')),
                'product_url': product_url,
                'product_image_url': product_image_url}
          
        next_page = response.xpath("//a[@class='page-link' and @rel='next']/@href").get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)