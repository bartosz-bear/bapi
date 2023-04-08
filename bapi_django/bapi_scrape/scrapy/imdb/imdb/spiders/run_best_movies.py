from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from bapi_scrape.scrapy.imdb.imdb.spiders.best_movies import BestMoviesSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from scrapy.settings import Settings

from bapi_django.settings.base import BASE_DIR

import os

def run_best_movies():

  #settings = get_project_settings()

  
  cwd = os.path.join(BASE_DIR, 'bapi_scrape\scrapy\imdb\imdb\spiders\\')

  print('BASE_DIR', BASE_DIR)
  print('FEEDS', 'file://' + cwd + "imbd_best_movies.json")
  
  settings={
    "FEEDS": {
        'file://' + cwd + "imbd_best_movies.json": {"format": "json"},
    },
    "ITEM_PIPELINES": {
        'imdb.pipelines.ImdbPipeline': 300,
    },
    "HTTPCACHE_ENABLED": True,
    "HTTPCACHE_EXPIRATION_SECS": 0,
    "HTTPCACHE_DIR": 'httpcache',
    "HTTPCACHE_IGNORE_HTTP_CODES": [],
    "HTTPCACHE_STORAGE": 'scrapy.extensions.httpcache.FilesystemCacheStorage',
    "FEED_EXPORT_ENCODING": 'utf-8'
  }
  

  #os.environ["SCRAPY_SETTINGS_MODULE"] = "bapi_scrape.scrapy.imdb.imdb"
  #os.environ["SCRAPY_PROJECT"] = "imdb"

  #settings = Settings()
  #settings_module_path = os.environ.get("SCRAPY_SETTINGS_MODULE")
  #if settings_module_path:
  #    settings.setmodule(settings_module_path, priority='spider')

  #settings = get_project_settings()

  #print('what is ENV', os.environ.get("SCRAPY_SETTINGS_MODULE"))
  #print('what is project ENV', os.environ.get("SCRAPY_PROJECT", "default"))

  #for s in settings:
  #  print(s)

  configure_logging(settings)
  runner = CrawlerRunner(settings)

  d = runner.crawl(BestMoviesSpider)
  d.addBoth(lambda _: reactor.stop())
  reactor.run() # the script will block here until the crawling is finished