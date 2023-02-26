from django.shortcuts import render
from django.http import HttpResponseRedirect
from bapi_scraping.scripts.coursera_scraper import scrap

from sqlalchemy import create_engine
from decouple import config

from .forms import CourseCategoriesForm

#from .queries.sqlalchemy.delete_courses_table import delete_courses_table
from .queries.psycopg2.delete_courses_table import delete_courses_table


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

    # Connect to a database and save data a new table
    #engine = create_engine("postgresql+psycopg2://" + config("DB_USER") + ":" + config("DB_PASSWORD") + "@localhost:" + config("DB_PORT") + "/" + config("DB_NAME"), echo=True)
    
    delete_courses_table()

    #delete_courses_table(engine)
    #context['courses'].to_sql('bapi_scraping_courses4', engine)

  else:
    form = CourseCategoriesForm()

  context['form'] = form

  return render(request, 'bapi_scraping/courses.html', context)