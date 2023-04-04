from django.shortcuts import render

def home(request):

  return render(request, 'home.html')

def scrape(request):

  return render(request, 'scrape.html')

def transform(request):

  return render(request, 'transform.html')

def load(request):
  context = {
    'page': 'Load Page'
  }
  return render(request, 'load.html', context)

def expose(request):
  context = {
    'page': 'Expose Page'
  }
  return render(request, 'expose.html', context)

def hire(request):
  context = {
    'page': 'Hire Page'
  }
  return render(request, 'hire.html', context)
