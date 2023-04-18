from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from bapi_load.scripts.db_operations import get_data

@csrf_exempt
def expose_best_movies(request):
  
  url = 'bapi_expose/movies/expose_best_movies.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('movies')}
      url = 'bapi_expose/movies/movies_table.html'

  return render(request, url, context=context)


@csrf_exempt
def expose_books(request):
  
  url = 'bapi_expose/books/expose_books.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('books')}
      url = 'bapi_expose/books/books_table.html'

  return render(request, url, context=context)

@csrf_exempt
def expose_writers(request):
  
  url = 'bapi_expose/writers/expose_writers.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('writers')}
      url = 'bapi_expose/writers/writers_table.html'

  return render(request, url, context=context)

@csrf_exempt
def expose_special_offers(request):
  
  url = 'bapi_expose/special_offers/expose_special_offers.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('special_offers')}
      url = 'bapi_expose/special_offers/special_offers_table.html'

  return render(request, url, context=context)

@csrf_exempt
def expose_fancy_glasses(request):
  
  url = 'bapi_expose/fancy_glasses/expose_fancy_glasses.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('fancy_glasses')}
      url = 'bapi_expose/fancy_glasses/fancy_glasses_table.html'

  return render(request, url, context=context)

@csrf_exempt
def expose_countries(request):
  
  url = 'bapi_expose/countries/expose_countries.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('countries')}
      url = 'bapi_expose/countries/countries_table.html'

  return render(request, url, context=context)

@csrf_exempt
def expose_debt_to_gdp(request):
  
  url = 'bapi_expose/debt_to_gdp/expose_debt_to_gdp.html'

  context = {}

  if request.method == 'POST':

      context = {'scraped': get_data('debt_to_gdp')}
      url = 'bapi_expose/debt_to_gdp/debt_to_gdp_table.html'

  return render(request, url, context=context)