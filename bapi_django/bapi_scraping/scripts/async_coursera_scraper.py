import requests
import aiohttp
import asyncio

from bs4 import BeautifulSoup

import pandas as pd

import re

ROOT = "https://www.coursera.org/"

async def async_get_course(session, url_course):
    async with session.get(url_course) as res:
        response = await res.content.read() 
        return response

async def async_get_course_infos(courses):

  # Use this line to control number of courses to fetch during debugging and development
  #courses = courses[:3]

  actions = []
  urls = []
  course_infos = []
  async with aiohttp.ClientSession() as session:
      for course in courses:
          url_course = f"{ROOT}{course['course_link']}"
          urls.append(url_course)
          actions.append(asyncio.ensure_future(async_get_course(session, url_course)))
      results = await asyncio.gather(*actions)

      for idx, res in enumerate(results):
          course_infos.append(get_info_from_course((courses[idx], urls[idx], res)))

  return course_infos


def get_summary_page(category):
    
    category = 'data-science'
    
    # Creating a BeautifulSoup object
    url_browse = f"{ROOT}browse/{category}"
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

    return courses

def get_info_from_course(response):
  # Scraping course page for each course. Updating 'Course Description', 'Enrollments' and 'Ratings'
  #for course in courses[:3]:

  course, _, course_response = response

  course_soup = BeautifulSoup(course_response, 'lxml', from_encoding='utf-8')
  course['instructor'] = get_course_instructor(course_soup)
  try:
    course['description'] = get_course_description(course_soup)
    course['students_enrolled'] = get_enrollments(course_soup)
    course['ratings'] = get_ratings(course_soup)
  except:
    course['description'] = "The course hasn't started yet."
    course['students_enrolled'] = "0"
    course['ratings'] = "0"

  return course


def get_course_instructor(soup):
    """
    Gets full description (all paragraphs) for a single course.
    """    
    try:
      instructor = soup.find('div', {'class': 'rc-BannerInstructorInfo'}).find('span').get_text()
      instructor = re.sub(r'\s\+\d+\s[\w\s]+', '', instructor)
      if instructor[-1] == ' ':
          instructor = instructor[:-1]
    except:
      instructor = "NA"

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

    courses = get_summary_page(category)

    print(courses)

    courses_final = asyncio.run(async_get_course_infos(courses))

    print(courses_final)

    # Converting a list of courses into pandas DataFrame; Cleaning data structure, formatting column headers
    df = pd.DataFrame(courses_final)
    df['Category Name'] = category
    df.drop('course_link', axis=1, inplace=True)
    df.rename(columns={'course_name': 'Course Name', 'instructor': 'First Instructor Name',
                       'description': 'Course Description',
                       'students_enrolled': '# of Students Enrolled', 'ratings': '# of Ratings'}, inplace=True)
    df = df.loc[:, ['Category Name', 'Course Name', 'First Instructor Name', 'Course Description',
                    '# of Students Enrolled', '# of Ratings']]
    df = df.drop_duplicates()

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

#scrap_and_close = scrap('data-science')