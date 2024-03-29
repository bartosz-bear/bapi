from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def table_exists(table_name):

  with db_cursor() as cur:

    cur.execute("SELECT * from information_schema.tables WHERE table_name=%s", (table_name,))
    if cur.fetchone()[0]:
      return True
    else:
      return False


def delete_table(table_name):

  with db_cursor() as cur:
    cur.execute('DROP TABLE %s;' % table_name)


def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              category VARCHAR(50) NOT NULL,
              course VARCHAR(150) NOT NULL,
              instructor VARCHAR(100) NOT NULL,
              description TEXT,
              enrollment_count INTEGER,
              rating INTEGER);
          ''' % table_name)


def insert_values(table_name, courses):

  with db_cursor() as cur:
    columns = courses.columns.values
    my_tuple = list(courses.itertuples(index=False, name=None))

    insert_query = '''INSERT INTO {} ({})
                      VALUES 
        '''.format(table_name, ', '.join(columns)) + ' %s'

    execute_values(cur, insert_query, my_tuple, template=None, page_size=100)

def get_courses_data(table_name):

  print(table_name)

  with db_cursor() as cur:

    cur.execute('SELECT * FROM %s;' % table_name)
    
    return cur.fetchall()