from django.urls import path

from . import views

app_name = 'bapi_scraping'
urlpatterns = [
  # /bapi_scraping
  path('', views.scraping_index, name='scraping_index'),
]