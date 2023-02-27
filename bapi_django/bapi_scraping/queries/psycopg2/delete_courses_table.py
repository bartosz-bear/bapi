import psycopg2
from decouple import config

from psycopg2.errors import UndefinedTable
from psycopg2.sql import SQL, Identifier
from psycopg2.extras import execute_values

def delete_courses_table(courses):

  conn = psycopg2.connect("dbname=" + config('DB_NAME') + " user=" + config('DB_USER') + " password=" + config('DB_PASSWORD'))
  cur = conn.cursor()

  __table_name__ = 'bapi_scraping_courses4'

  try:
    cur.execute('DROP TABLE %s;' % __table_name__)
    conn.commit()
  except Exception as e:
    if type(e) == UndefinedTable:

      conn.rollback()
      cur.execute('''CREATE TABLE %s (
                     id SERIAL PRIMARY KEY,
                     category VARCHAR(50) NOT NULL,
                     course VARCHAR(150) NOT NULL UNIQUE,
                     instructor VARCHAR(100) NOT NULL,
                     description TEXT,
                     enrollment_count INTEGER,
                     rating INTEGER);
                  ''' % __table_name__)
      
      columns = courses.columns.values
      my_tuple = list(courses.itertuples(index=False, name=None))

      insert_query = '''INSERT INTO {} ({})
                     VALUES 
      '''.format(__table_name__, ', '.join(columns)) + ' %s'

      execute_values(cur, insert_query, my_tuple, template=None, page_size=100)

      conn.commit()
      
    else:
      print(e)
      print(type(e))
      print(str(e))
      print(repr(e))

  cur.close()
  conn.close()

  return

'''
def insert_courses(courses):

  return
'''