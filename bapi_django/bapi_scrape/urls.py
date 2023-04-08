from django.urls import path

from . import views

app_name = 'bapi_scrape'
urlpatterns = [
  path('scrape/courses/', views.scrape_courses, name='scrape_courses'),
  path('scrape/movies/', views.scrape_movies, name='scrape_movies'),
  path('scrape/movies/run_spider', views.run_spider, name='run_spider')
]