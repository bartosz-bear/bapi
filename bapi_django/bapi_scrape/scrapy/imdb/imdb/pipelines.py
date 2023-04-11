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