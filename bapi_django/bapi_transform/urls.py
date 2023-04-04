from django.urls import path

from . import views

app_name = 'bapi_transform'
urlpatterns = [
  path('transform/financial_transactions/', views.checks, name='checks')
]