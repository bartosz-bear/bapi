from django.urls import path

from . import views

app_name = 'bapi_django_app'
urlpatterns = [
  # /bapi_django_app
  path('home/', views.index, name='index'),
]