from django.urls import path

from . import views

app_name = 'bapi_master'
urlpatterns = [
  path('about/', views.about, name='about'),
  path('scrape/', views.scrape, name='scrape'),
  path('transform/', views.transform, name='transform'),
  path('load/', views.load, name='load'),
  path('expose/', views.expose, name='expose'),
  path('contact/', views.contact, name='contact'),
]