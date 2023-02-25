from django.shortcuts import render
from django.http import HttpResponseRedirect
from bapi_scraping.scripts.coursera_scraper import scrap, get_dropdown_choices
#from django.views.decorators.csrf import csrf_protect

from decouple import config

from .forms import NameForm

def scraping_index(request):

  select_input_options = ""
  for key, value in get_dropdown_choices().items():
    select_input_options += f"<option value='{value}'>{key}</option>"

  selection_form = ''' <form method="post" action="/bapi_scraping/get_courses">
                          {% csrf_token %}
                          <p><b>It will take up to 2 minutes to scrap data and create a CSV file.
                           After you press the button, do not refresh the page.</b><p>
                          <label for="course_category">Choose a course category:</label>
                          <select name="course_category">''' + select_input_options + '''</select><input type="submit"/></form>'''

  context = {
    'my_name': 'Bartosz',
    'course_categories': get_dropdown_choices(),
    'select_input_options': select_input_options,
    'selection_form': selection_form
  }
  return render(request, 'bapi_scraping/index.html', context)

def get_courses(request):

  context = {}

  if request.method == 'POST':
    form = NameForm(request.POST)
    context['final_choice'] = request.POST['choice']
    print('users choice       ', request.POST['choice'])
    courses = scrap(request.POST['choice'])
    context['courses'] = courses
    

    print('is it a dataframe?', type(courses))
    
    from sqlalchemy import create_engine
    postgres_user = config("DB_USER")
    postgres_password = config("DB_PASSWORD")
    engine = create_engine("postgresql+psycopg2://" + config("DB_USER") + ":" + config("DB_PASSWORD") + "@localhost:" + config("DB_PORT") + "/" + config("DB_NAME"))

    courses.to_sql('bapi_scraping_courses2', engine)

    #DB_HOST = "127.0.0.1"
    
    #courses.to_sql()

    #if form.is_valid():
    #  return HttpResponseRedirect('/thanks')

  else:
    form = NameForm()

  context['form'] = form

  print(context)

  return render(request, 'bapi_scraping/courses.html', context)









#######################

def get_name(request):
  if request.method == 'POST':
    form = NameForm(request.POST)

    if form.is_valid():
      return HttpResponseRedirect('/thanks')
    
  else:
    form = NameForm()

  return render(request, 'bapi_scraping/name.html', {'form': form})