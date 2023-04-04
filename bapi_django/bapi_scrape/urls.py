from django.urls import path

from . import views

app_name = 'bapi_scrape'
urlpatterns = [
  path('scrape/courses/', views.scrape_courses, name='scrape_courses')
]