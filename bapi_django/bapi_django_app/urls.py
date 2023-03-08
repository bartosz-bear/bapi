from django.urls import path

from . import views

app_name = 'bapi_django_app'
urlpatterns = [
  # /bapi_django_app
  path('home/', views.home, name='home'),
  path('transform/', views.transform, name='transform'),
  path('load/', views.load, name='load'),
  path('visualize/', views.visualize, name='visualize'),
  path('hire/', views.hire, name='hire'),
]