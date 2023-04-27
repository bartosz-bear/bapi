# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bapi_django.queries.pools import db_cursor
from bapi_load.scripts.movies.db_operations import create_table as create_movies_table
from bapi_load.scripts.books.db_operations import create_table as create_books_table
from bapi_load.scripts.writers.db_operations import create_table as create_writers_table
from bapi_load.scripts.special_offers.db_operations import create_table as create_special_offers_table
from bapi_load.scripts.fancy_glasses.db_operations import create_table as create_fancy_glasses_table
from bapi_load.scripts.countries.db_operations import create_table as create_countries_table
from bapi_load.scripts.debt_to_gdp.db_operations import create_table as create_debt_to_gdp_table
from bapi_load.scripts.stackoverflow.db_operations import create_table as create_stackoverflow_table

class ImdbPipeline:
    
    def __init__(self):
      #create_movies_table('movies')
      pass
         
    def process_item(self, item, spider):
                
      with db_cursor() as cur:
        cur.execute("""INSERT INTO movies (title, year, duration, genre, rating, movie_url) VALUES (%s,%s,%s,%s,%s,%s);""", (
            item["title"],
            item["year"],
            item["duration"],
            item["genre"],
            item["rating"],
            item["movie_url"]
        ))

      return item

    def close_spider(self, spider):
        pass

class BooksPipeline:
   
  def __init__(self):
    #create_books_table('books')
    pass
   
  def process_item(self, item, spider):
      
    with db_cursor() as cur:
      cur.execute("""INSERT INTO books (name, price) VALUES (%s,%s);""", (
          item["name"],
          item["price"]
      ))

    return item
   
  def close_spider(self, spider):
    pass

class WritersPipeline:

  def __init__(self):
    #create_writers_table('writers')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO writers (quote, author, tags) VALUES (%s, %s, %s);""", (
        item['quote'],
        item['author'],
        item['tags']
      ))

    return item
  
  def close_spider(self, spider):
    pass


class SpecialOffersPipeline:

  def __init__(self):
    #create_special_offers_table('special_offers')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO special_offers (name, link, special_price, normal_price) VALUES (%s, %s, %s, %s);""", (
        item['name'],
        item['link'],
        item['special_price'],
        item['normal_price']
      ))

    return item
  
  def close_spider(self, spider):
    pass

class FancyGlassesPipeline:

  def __init__(self):
    #create_fancy_glasses_table('fancy_glasses')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO fancy_glasses (name, price, product_url, product_image_url) VALUES (%s, %s, %s, %s);""", (
        item['name'],
        item['price'],
        item['product_url'],
        item['product_image_url']
      ))

    return item
  
  def close_spider(self, spider):
    pass

class CountriesPipeline:

  def __init__(self):
    #create_countries_table('countries')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO countries (country, year, population) VALUES (%s, %s, %s);""", (
        item['country'],
        item['year'],
        item['population']
      ))

    return item
  
  def close_spider(self, spider):
    pass

class DebtToGDPPipeline:

  def __init__(self):
    #create_debt_to_gdp_table('debt_to_gdp')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO debt_to_gdp (country, debt_to_gdp) VALUES (%s, %s);""", (
        item['country'],
        item['debt_to_gdp']
      ))

    return item
  
  def close_spider(self, spider):
    pass

class StackOverflowPipeline:

  def __init__(self):
    create_stackoverflow_table('stackoverflow')
    pass

  def process_item(self, item, spider):

    with db_cursor() as cur:
      cur.execute("""INSERT INTO stackoverflow (date, tag, questions) VALUES (%s, %s, %s);""", (
        item['date'],
        item['tag'],
        item['questions']
      ))

    return item
  
  def close_spider(self, spider):
    pass