from django.urls import path

from . import views

app_name = 'bapi_django_app'
urlpatterns = [
  # /bapi_django_app
  path('', views.index, name='index'),
  # eg. /bapi_django_app/5/
  path('<int:question_id>/', views.detail, name='detail'),
  # eg. /bapi_django_app/5/results/
  path('<int:question_id>/results/', views.results, name='results'),
  # ex. /bapi_django_app/vote/
  path('<int:question_id>/vote/', views.vote, name='vote')
]