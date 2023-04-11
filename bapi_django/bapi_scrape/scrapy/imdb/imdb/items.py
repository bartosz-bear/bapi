# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class ImdbItem(Item):
    title = Field()
    year = Field()
    duration = Field()
    genre = Field()
    rating = Field()
    movie_url = Field()

class BooksItem(Item):
    name = Field()
    price = Field()

class WritersItem(Item):
    quote = Field()
    author = Field()
    tags = Field()

class SpecialOffersItem(Item):
    name = Field()
    link = Field()
    special_price = Field()
    normal_price = Field()