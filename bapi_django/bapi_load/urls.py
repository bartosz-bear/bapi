from django.urls import path

from . import views

app_name = 'bapi_load'
urlpatterns = [
  path('load/load_transactions/', views.load_transactions, name='load_transactions')
]