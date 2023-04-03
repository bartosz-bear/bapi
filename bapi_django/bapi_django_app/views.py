from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from bapi_django_app.scripts.transform_finance import transform_finance
from bapi_django_app.queries.psycopg2.save_finance import insert_values, insert_values_multi, create_table, delete_table
from bapi_django_app.scripts.insert_finance_tables import insert_tables

from .models import Question


def home(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #template = loader.get_template('bapi_django_app/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  return render(request, 'home.html', context)

def transform(request):

  context = {}

  if request.method == 'POST':

    checks = transform_finance()
    #insert_tables(checks)

    context['checks'] = checks['checks_summary']

  return render(request, 'transform.html', context)

def load(request):
  context = {
    'page': 'Load Page'
  }
  return render(request, 'load.html', context)

def visualize(request):
  context = {
    'page': 'Visualize Page'
  }
  return render(request, 'visualize.html', context)

def hire(request):
  context = {
    'page': 'Hire Page'
  }
  return render(request, 'hire.html', context)
