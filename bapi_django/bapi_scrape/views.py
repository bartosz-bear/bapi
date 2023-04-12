from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import CourseCategoriesForm

from bapi_scrape.scripts.courses.scrape import scrape
from bapi_load.scripts.courses.db_operations import insert_values, create_table, delete_table, get_courses_data
from bapi_load.scripts.db_operations import get_data
from bapi_load.scripts.movies.db_operations import get_data as get_data_movies
from bapi_load.scripts.books.db_operations import get_data as get_data_books

from psycopg2.errors import DuplicateTable
from psycopg2.errors import UniqueViolation

from scrapyd_api import ScrapydAPI

from decouple import config
import time

SCRAPYD_HOST = config('SCRAPYD_HOST')


## COURSES SCRIPT
def scrape_courses(request):
  '''
  View displays course categories available at Coursera and allows user to choose the category of courses he would like to scrap
  ''' 

  context = {}

  if request.method == 'POST':
    form = CourseCategoriesForm(request.POST)

    # Get user's choice from the POST request and use it to scrap data from Coursera
    context['final_choice'] = request.POST['choice']
    context['courses'] = scrape(request.POST['choice'])
    context['courses'].rename(columns={'Category Name': 'category', 'Course Name':'course','First Instructor Name': 'instructor',
                                       'Course Description': 'description', '# of Students Enrolled': 'enrollment_count',
                                       '# of Ratings': 'rating'}, inplace=True)

    try:
      create_table('coursera_courses')
      insert_values('coursera_courses', context['courses'])
    except DuplicateTable or UniqueViolation:
      delete_table('coursera_courses')
      create_table('coursera_courses')
      insert_values('coursera_courses', context['courses'])

      context['scraped'] = get_courses_data('coursera_courses')

    context['call_to_action'] = '''And there you have it. Imagine how much time it would take to collect this data by hand. If you are quick with your mouse, it would take you probably about 30 seconds
                                   for one course to copy-paste this information to your Excel. You would need 30 minutes of labor work to collect information about 60 courses. It takes 5-10 seconds
                                   with web scraping. And another good thing, web scraping scales really well - it doesn't matter if you collect 60 courses, 600 or 6000, it would take about the same 5-10
                                   seconds to collect.'''
      
    context['call_to_action2'] = '''I design web scraping solutions JUST FOR YOUR NEEDS. Curious if I can help you? Email me at <a href="mailto:bartosz.artur.piechnik@gmail.com">bartosz.artur.piechnik@gmail.com</a>'''

  else:
    form = CourseCategoriesForm()

  context['form'] = form

  return render(request, 'bapi_scrape/courses/scrape.html', context)

## MOVIES CRAWLER
def scrape_movies(request):

  return render(request, 'bapi_scrape/movies/scrape_movies.html')

@csrf_exempt
def run_spider(request):

  scrapyd = ScrapydAPI(config('SCRAPYD_HOST'))
  scrapyd.schedule('imdb', 'best_movies')

  job_id = scrapyd.list_jobs('imdb')['pending'][0]['id']
  if not job_id:
    job_id = scrapyd.list_jobs('imdb')['running'][0]['id']
  
  while scrapyd.job_status('imdb', job_id) != 'finished':
    time.sleep(0.5)

  context = {'scraped': get_data('movies')}
  
  return render(request, 'bapi_scrape/movies/movies_table.html', context=context)

## BOOKS SPIDER
def scrape_books(request):

  return render(request, 'bapi_scrape/books/scrape_books.html')

@csrf_exempt
def run_books_spider(request):

  scrapyd = ScrapydAPI(config('SCRAPYD_HOST'))
  scrapyd.schedule('imdb', 'books')

  job_id = scrapyd.list_jobs('imdb')['pending'][0]['id']
  if not job_id:
    job_id = scrapyd.list_jobs('imdb')['running'][0]['id']

  while scrapyd.job_status('imdb', job_id) != 'finished':
    time.sleep(0.5)

  context = {'scraped': get_data('books')}

  return render(request, 'bapi_scrape/books/books_table.html', context=context)

## WRITERS SPIDER
def scrape_writers(request):

  return render(request, 'bapi_scrape/writers/scrape_writers.html')

@csrf_exempt
def run_writers_spider(request):

  scrapy_d = innit_scrapyd(SCRAPYD_HOST, 'imdb', 'writers')

  context = {'scraped': get_data('writers')}

  return render(request, 'bapi_scrape/writers/writers_table.html', context=context)

# SPECIAL OFFERS SPIDER
def scrape_special_offers(requst):

  return render(requst, 'bapi_scrape/special_offers/scrape_special_offers.html')

@csrf_exempt
def run_special_offers_spider(request):

  scrapy_d = innit_scrapyd(SCRAPYD_HOST, 'imdb', 'special_offers')

  context = {'scraped': get_data('special_offers')}

  return render(request, 'bapi_scrape/special_offers/special_offers_table.html', context=context)

# FANCY GLASSES SPIDER
def scrape_fancy_glasses(requst):

  return render(requst, 'bapi_scrape/fancy_glasses/scrape_fancy_glasses.html')

@csrf_exempt
def run_fancy_glasses_spider(request):

  scrapy_d = innit_scrapyd(SCRAPYD_HOST, 'imdb', 'fancy_glasses')

  context = {'scraped': get_data('fancy_glasses')}

  return render(request, 'bapi_scrape/fancy_glasses/fancy_glasses_table.html', context=context)

# COUNTRIES SPIDER
def scrape_countries(requst):

  return render(requst, 'bapi_scrape/countries/scrape_countries.html')

@csrf_exempt
def run_countries_spider(request):

  scrapy_d = innit_scrapyd(SCRAPYD_HOST, 'imdb', 'countries')

  context = {'scraped': get_data('countries')}

  return render(request, 'bapi_scrape/countries/countries_table.html', context=context)

# DEBT-TO-GDP SPIDER
def scrape_debt_to_gdp(requst):

  return render(requst, 'bapi_scrape/debt_to_gdp/scrape_debt_to_gdp.html')

@csrf_exempt
def run_debt_to_gdp_spider(request):

  scrapy_d = innit_scrapyd(SCRAPYD_HOST, 'imdb', 'debt_to_gdp')

  context = {'scraped': get_data('debt_to_gdp')}

  return render(request, 'bapi_scrape/debt_to_gdp/debt_to_gdp_table.html', context=context)




def innit_scrapyd(host, project_name, spider_name, delay=0.5):

  scrapyd = ScrapydAPI(host)
  scrapyd.schedule(project_name, spider_name)

  job_id = scrapyd.list_jobs(project_name)['pending'][0]['id']
  if not job_id:
    job_id = scrapyd.list_jobs(project_name)['running'][0]['id']

  while scrapyd.job_status(project_name, job_id) != 'finished':
    time.sleep(delay)

  return scrapyd


