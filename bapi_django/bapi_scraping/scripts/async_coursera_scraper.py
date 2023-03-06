from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

import pandas as pd

import aiohttp
import asyncio
import time

async def main(course, root):
    
    
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.coursera.org/browse/data-science') as response:
            
            #print('Status:', response.status)
            #print('Content-type', response.headers['content-type'])

            html = await response.text()
            #print('Body:', html[:15], "...")

            #print('Response text:', html)

#####################################################################################################

async def async_get_course(session, url_course):
    #url_course = f"{root}{course['course_link']}"
    async with session.get(url_course) as res:
        response = await res.content.read() 
        return response

async def example(courses, root):

  starting_time = time.time()
    
  actions = []
  data = []
  data2 = []
  async with aiohttp.ClientSession() as session:
      for course in courses:
          url_course = f"{root}{course['course_link']}"
          data.append(url_course)
          actions.append(asyncio.ensure_future(async_get_course(session, url_course)))
      results = await asyncio.gather(*actions)
      
      for idx, res in enumerate(results):
          #html = await res.text()
          #print('what is d', d)
          data2.append(get_info_from_course((courses[idx], data[idx], res)))
  #print('finalllyyyy', data2)

  total_time = time.time() - starting_time
  print('total_time', total_time)

  return data2

def get_course(course, root):
  # Request data for an individual course

  url_course = f"{root}{course['course_link']}"
  response = requests.get(url_course)

  return course, url_course, response

def get_info_from_course(response):
  # Scraping course page for each course. Updating 'Course Description', 'Enrollments' and 'Ratings'
  #for course in courses[:3]:

  course, url_course, course_response = response

  #print('course response yyyyyyyyyyyyyy', course, url_course, type(course_response))

  course_soup = BeautifulSoup(course_response, 'lxml', from_encoding='utf-8')
  course['instructor'] = get_course_instructor(url_course)
  try:
    course['description'] = get_course_description(course_soup)
    course['students_enrolled'] = get_enrollments(course_soup)
    course['ratings'] = get_ratings(course_soup)
  except:
    course['description'] = "The course hasn't started yet."
    course['students_enrolled'] = "0"
    course['ratings'] = "0"
    
  return course

def get_course_instructor(course_path):
    """
    Gets name of the first instructor for a single course.
    """
    page = urlopen(course_path).read()
    soup = BeautifulSoup(page, 'lxml')
    instructor = soup.find('h3', {'class': 'instructor-name headline-3-text bold'}).get_text().split('Top')[0]

    return instructor


def get_course_description(soup):
    """
    Gets full description (all paragraphs) for a single course.
    """
    descriptions_html_block = soup.find_all('div', {'class': 'content-inner'})
    html_paragraphs = descriptions_html_block[0].find_all('p')

    string_paragraphs = []
    for i in html_paragraphs:
        string_paragraphs.append(i.get_text())

    course_description = ''.join(string_paragraphs)

    return course_description


def get_enrollments(soup):
    """
    Gets number of enrolled students in a single course.
    """
    enrollments_as_str = soup.find('div', {'class': 'rc-ProductMetrics'}).find('strong').find('span').get_text()
    enrollments = int(enrollments_as_str.replace(',', ''))
    return enrollments


def get_ratings(soup):
    """
    Gets ratings of a single course.
    """
    ratings_as_str = soup.find('span', {'data-test': 'ratings-count-without-asterisks'}).find('span').get_text()
    ratings = int(ratings_as_str.strip(' ratings').replace(',', ''))
    return ratings


def scrap(category):
    """
    Gets a single course category and saves all courses from this category as .csv file. Returns a list of courses
    with features.

    CSV file contains following categories: Course Name, Course Category, Instructor, Description, # of Students
    Enrolled, # of Ratings.

    In case, the course hasn't started yet (therefore has no ratings and no students enrolled), this information
    is shown in the .csv file in the following way: "Description": "The course hasn't started yet", "# of Students
    Enrolled": 0, "# of Ratings": 0

    DISCLAIMER: This function is designed to work with the server back end. In order to run it locally, pass the
    category argument in the following format: scrap('data-science')
    """

    # Creating a BeautifulSoup object
    root = "https://www.coursera.org/"
    url_browse = f"{root}browse/{category}"
    request_browse = requests.get(url_browse)
    browse_soup = BeautifulSoup(request_browse.content, 'lxml', from_encoding='utf-8')

    # Finding a product card for each course
    course_html_containers = browse_soup.find_all('div', {'class': 'rc-ProductCard'})

    # Scraping 'Course Name' and 'Course Link' for each course found in Coursera's summary page
    courses = []
    for i, j in enumerate(course_html_containers):
        course_type = j.find('label', {'class': 'rc-CardText css-1feobmm'}).get_text()
        if course_type == 'Course':
            course_features = dict(course_name='', course_link='')
            course_features['course_name'] = j.find('a', {'class': 'CardText-link'}).get_text()
            course_features['course_link'] = j.find('a', {'class': 'CardText-link'})['href']
            courses.append(course_features)

    #courses = courses[:2]

    courses_final = asyncio.run(example(courses, root))

    #print('working xxxxxxx', courses_final)

    '''
    # Get course info for each course in the category
    courses_final = []
    for course in courses[:2]:
        #courses_final.append(get_course(course, root))
        courses_final.append(get_info_from_course(get_course(course, root)))
    '''

    # Converting a list of courses into pandas DataFrame; Cleaning data structure, formatting column headers
    df = pd.DataFrame(courses_final)
    df['Category Name'] = category
    
    df.drop('course_link', axis=1, inplace=True)
    df.rename(columns={'course_name': 'Course Name', 'instructor': 'First Instructor Name',
                       'description': 'Course Description',
                       'students_enrolled': '# of Students Enrolled', 'ratings': '# of Ratings'}, inplace=True)
    df = df.loc[:, ['Category Name', 'Course Name', 'First Instructor Name', 'Course Description',
                    '# of Students Enrolled', '# of Ratings']]

    print(df.head())

    # Saving to .csv
    #df.to_csv('courses_final.csv', index=False)

    # Printing summary information
    print(f'DONE! There are {len(courses_final)} courses in the category {category}.')

    return df


def get_dropdown_choices():
    """
    Gets each course category available in Coursera and returns a list which can be used as a dropdown list on the
    front end.
    DISCLAIMER: 'data-science' as a single value is hardcoded in the 'categories' value, as this element wasn't
    possible to get without using Selenium.
    """
    url_browse = "https://www.coursera.org/browse"
    request = requests.get(url_browse)
    soup = BeautifulSoup(request.content, 'lxml', from_encoding='utf-8')

    categories = soup.find_all('div', {'class': 'topic-column'})

    # data-science is hardcoded
    categories_list = ['data-science']
    for c in categories:
        categories_list.append(c.find('a')['to'][8:])

    categories_dict = {}
    for c in categories_list:
        categories_dict[c.replace('-', ' ').capitalize()] = c

    return categories_dict

scrap_and_close = scrap('data-science')


#####################################################################################################

'''
if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  try:
      asyncio.run(main())
  except KeyboardInterrupt:
      pass
'''
