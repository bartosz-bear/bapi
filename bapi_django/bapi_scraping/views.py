from django.shortcuts import render
from django.http import HttpResponseRedirect
from bapi_scraping.scripts.coursera_scraper import scrap

from decouple import config

from .forms import CourseCategoriesForm

from .queries.psycopg2.courses_queries import insert_values, create_table, delete_table, get_data


def scraping_index(request):
  '''
  Main view for scraping related functionalities
  '''

  context = {
    'my_name': 'Bartosz',
  }
  return render(request, 'bapi_scraping/index.html', context)


def get_courses(request):
  '''
  View displays course categories available at Coursera and allows user to choose the category of courses he would like to scrap
  ''' 

  context = {}

  if request.method == 'POST':
    form = CourseCategoriesForm(request.POST)

    # Get user's choice from the POST request and use it to scrap data from Coursera
    context['final_choice'] = request.POST['choice']
    context['courses'] = scrap(request.POST['choice'])
    context['courses'].rename(columns={'Category Name': 'category', 'Course Name':'course','First Instructor Name': 'instructor',
                                       'Course Description': 'description', '# of Students Enrolled': 'enrollment_count',
                                       '# of Ratings': 'rating'}, inplace=True)

    try:
      create_table('bapi_scraping_courses2')
      insert_values('bapi_scraping_courses2', context['courses'])
      print('table created and populated')
    except:
      delete_table('bapi_scraping_courses2')
      create_table('bapi_scraping_courses2')
      insert_values('bapi_scraping_courses2', context['courses'])

      context['scraped'] = get_data('bapi_scraping_courses2')

      print('scraped data', context['scraped'])

      print('del cre ins')
      
  else:
    form = CourseCategoriesForm()

  context['form'] = form

  return render(request, 'bapi_scraping/courses.html', context)