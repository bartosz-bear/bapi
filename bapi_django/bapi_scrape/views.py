from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import CourseCategoriesForm

from bapi_scrape.scripts.courses.scrape import scrape
from bapi_load.scripts.courses.db_operations import insert_values, create_table, delete_table, get_data

from psycopg2.errors import DuplicateTable
from psycopg2.errors import UniqueViolation

import scrapy
from scrapy.crawler import CrawlerRunner
from bapi_scrape.scrapy.imdb.imdb.spiders.best_movies import BestMoviesSpider
from scrapy.utils.log import configure_logging

from twisted.internet import reactor


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

      context['scraped'] = get_data('coursera_courses')

    context['call_to_action'] = '''And there you have it. Imagine how much time it would take to collect this data by hand. If you are quick with your mouse, it would take you probably about 30 seconds
                                   for one course to copy-paste this information to your Excel. You would need 30 minutes of labor work to collect information about 60 courses. It takes 5-10 seconds
                                   with web scraping. And another good thing, web scraping scales really well - it doesn't matter if you collect 60 courses, 600 or 6000, it would take about the same 5-10
                                   seconds to collect.'''
      
    context['call_to_action2'] = '''I design web scraping solutions JUST FOR YOUR NEEDS. Curious if I can help you? Email me at <a href="mailto:bartosz.artur.piechnik@gmail.com">bartosz.artur.piechnik@gmail.com</a>'''

  else:
    form = CourseCategoriesForm()

  context['form'] = form

  return render(request, 'bapi_scrape/courses/scrape.html', context)

def scrape_movies(request):

  context = {'movies': '<p>LALLAA</p>'}

  return render(request, 'bapi_scrape/movies/scrape.html', context)

@csrf_exempt
def run_spider(request):

  configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
  runner = CrawlerRunner()

  d = runner.crawl(BestMoviesSpider)
  d.addBoth(lambda _: reactor.stop())
  reactor.run()

  return render(request, 'bapi_scrape/movies/movies_table.html')










def swap_element(request):

  return render(request, 'bapi_scrape/movies/swap.html')

def show_spinner(request):

  return render(request, 'bapi_scrape/movies/show_spinner.html')