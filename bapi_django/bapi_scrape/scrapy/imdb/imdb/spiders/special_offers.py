import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]

    custom_settings = {'ITEM_PIPELINES': {
       'imdb.pipelines.SpecialOffersPipeline': 300
    }}

    def start_requests(self):
        yield scrapy.Request(url='https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html',
                             callback=self.parse,
                             headers={
                                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                             })

    def parse(self, response):

        products = response.xpath(
            '//div[@class="r_b_c"]/ul[@class="productlisting-ul"]/div[@class="p_box_wrapper"]/li[@class="productListing-even"]')

        for product in products:
            name = product.xpath('.//a[@class="p_box_title"]/text()').get()
            link = product.xpath('.//a[@class="p_box_title"]/@href').get()
            special_price = product.xpath(
                './/div[@class="p_box_price"]/span[@class="productSpecialPrice fl"]/text()').get()
            normal_price = product.xpath(
                './/div[@class="p_box_price"]/span[@class="normalprice fl"]/text()').get()

            yield {'name': name,
                   'link': link,
                   'special_price': float(special_price.replace('$', '')),
                   'normal_price': float(normal_price.replace('$', ''))}

        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
            })