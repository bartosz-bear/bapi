from django.urls import path

from . import views

app_name = 'bapi_scrape'
urlpatterns = [
  path('scrape/courses/', views.scrape_courses, name='scrape_courses'),
  path('scrape/movies/', views.scrape_movies, name='scrape_movies'),
  path('scrape/movies/run_spider', views.run_spider, name='run_spider'),
  path('scrape/books/', views.scrape_books, name='scrape_books'),
  path('scrape/books/run_books_spider', views.run_books_spider, name='run_books_spider'),
  path('scrape/writers/', views.scrape_writers, name='scrape_writers'),
  path('scrape/writers/run_writers_spider', views.run_writers_spider, name='run_writers_spider'),
  path('scrape/special_offers/', views.scrape_special_offers, name='scrape_special_offers'),
  path('scrape/special_offers/run_special_offers_spider', views.run_special_offers_spider, name='run_special_offers_spider'),
  path('scrape/fancy_glasses/', views.scrape_fancy_glasses, name='scrape_fancy_glasses'),
  path('scrape/fancy_glasses/run_fancy_glasses_spider', views.run_fancy_glasses_spider, name='run_fancy_glasses_spider'),
  path('scrape/countries/', views.scrape_countries, name='scrape_countries'),
  path('scrape/countries/run_countries_spider', views.run_countries_spider, name='run_countries_spider'),
  path('scrape/debt_to_gdp/', views.scrape_debt_to_gdp, name='scrape_debt_to_gdp'),
  path('scrape/debt_to_gdp/run_debt_to_gdp_spider', views.run_debt_to_gdp_spider, name='run_debt_to_gdp_spider')
]