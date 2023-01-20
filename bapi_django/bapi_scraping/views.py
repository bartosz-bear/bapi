from django.shortcuts import render
from bapi_scraping.scripts.coursera_scraper import scrap

def scraping_index(request):
  context = {
    'my_name': 'Bartosz'
  }
  return render(request, 'bapi_scraping/index.html', context)