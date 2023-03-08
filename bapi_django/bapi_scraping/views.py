from django.shortcuts import render

from .forms import CourseCategoriesForm

from bapi_scraping.scripts.async_coursera_scraper import scrap

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
      create_table('coursera_courses')
      insert_values('coursera_courses', context['courses'])
    except:
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

  return render(request, 'bapi_scraping/courses.html', context)