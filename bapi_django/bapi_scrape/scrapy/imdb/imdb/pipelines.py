# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bapi_django.queries.pools import db_cursor
from bapi_load.scripts.books.db_operations import create_table

class ImdbPipeline:
    
    def __init__(self):
      #create_table('movies')
      pass
         
    def process_item(self, item, spider):
                
      with db_cursor() as cur:
        cur.execute(""" INSERT INTO movies (title, year, duration, genre, rating, movie_url) VALUES (%s,%s,%s,%s,%s,%s);""", (
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
    #create_table('books')
    pass
   
  def process_item(self, item, spider):
      
    with db_cursor() as cur:
      cur.execute(""" INSERT INTO books (name, price) VALUES (%s,%s);""", (
          item["name"],
          item["price"]
      ))

    return item
   
  def close_spider(self, spider):
    pass