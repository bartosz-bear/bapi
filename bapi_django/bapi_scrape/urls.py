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
  path('scrape/writers/run_writers_spider', views.run_writers_spider, name='run_writers_spider')
]