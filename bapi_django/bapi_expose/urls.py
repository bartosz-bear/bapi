from django.urls import path

from . import views

app_name = 'bapi_expose'
urlpatterns = [
  path('expose/expose_best_movies/', views.expose_best_movies, name='expose_best_movies'),
  path('expose/expose_books/', views.expose_books, name='expose_books'),
  path('expose/expose_writers/', views.expose_writers, name='expose_writers'),
  path('expose/expose_special_offers/', views.expose_special_offers, name='expose_special_offers'),
  path('expose/expose_fancy_glasses/', views.expose_fancy_glasses, name='expose_fancy_glasses'),
  path('expose/expose_countries/', views.expose_countries, name='expose_countries'),
  path('expose/expose_debt_to_gdp/', views.expose_debt_to_gdp, name='expose_debt_to_gdp'),
]