from django.shortcuts import render, redirect

def home(request):

  return redirect('/about/')

def about(request):

  return render(request, 'about.html')

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

def contact(request):
  context = {
    'page': 'Contact Page'
  }
  return render(request, 'contact.html', context)
