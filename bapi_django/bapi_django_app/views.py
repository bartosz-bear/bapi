from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question


def home(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #template = loader.get_template('bapi_django_app/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  return render(request, 'home.html', context)

def transform(request):
  context = {
    'page': 'Transform Page'
  }
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
