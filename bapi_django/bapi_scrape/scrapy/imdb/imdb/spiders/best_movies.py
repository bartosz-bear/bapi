import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',
                             headers={'User-Agent': self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent')
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        
        container = response.xpath("//div[@class='ipc-page-content-container ipc-page-content-container--center'][2]")

        title = container.xpath(".//section/section/div[2]/div/h1/span/text()").get()
        if not title:
          title = container.xpath(".//section/section/div[2]/div/h1/text()").get()

        year = container.xpath(".//section/section/div[2]/div/ul/li/a/text()").get()
        if not year:
          year = container.xpath(".//section/section/div[2]/div/div//ul/li/a/text()").get()

        duration = container.xpath(".//section/section/div[2]/div/ul/li[3]/text()").get()
        if not duration:
          duration = container.xpath(".//section/section/div[2]/div/div/ul/li[3]/text()").extract()
          del duration[2]
          duration = ' '.join(duration)

        genre = container.xpath(".//section/section/div[3]/div[2]/div/section/div/div[2]/a[1]/span/text()").get()
        if not genre:
          genre = container.xpath(".//section/section/div[3]/div[2]/div/div/div/div/a/span/text()").get()

        rating = container.xpath(".//section/section/div[3]/div[2]/div/div/div//div[2]/div/span/text()").get()

        yield {
            'title': title,
            'year': year,
            'duration': duration,
            'genre': genre,
            'rating': rating,
            'movie_url': response.url,
            'user_agent': response.request.headers['User-Agent'].decode('utf-8')
        }