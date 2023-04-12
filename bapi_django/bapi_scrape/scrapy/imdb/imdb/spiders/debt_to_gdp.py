import scrapy

class DebtToGDPSpider(scrapy.Spider):
    name = 'debt_to_gdp'
    allowed_domains = ['www.tradingeconomics.com']
    start_urls = ['https://www.tradingeconomics.com/country-list/government-debt-to-gdp']

    custom_settings = {'ITEM_PIPELINES': {
       'imdb.pipelines.DebtToGDPPipeline': 300
    }}

    def parse(self, response):
        
        rows = response.xpath('//table/tr')

        for row in rows:
            country_name = row.xpath(".//td[1]/a").xpath("normalize-space()").get()
            debt_to_gdp = row.xpath(".//td[2]/text()").get()

            yield {
                'country': country_name,
                'debt_to_gdp': float(debt_to_gdp)
            }