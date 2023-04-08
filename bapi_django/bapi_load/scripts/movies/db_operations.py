from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def delete_table(table_name):

  with db_cursor() as cur:
    cur.execute('DROP TABLE %s;' % table_name)


def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              title VARCHAR(50) NOT NULL,
              year INT,
              duration VARCHAR(50),
              genre VARCHAR(50),
              rating DECIMAL(10,1),
              movie_url VARCHAR(250));
          ''' % table_name)


def insert_values(table_name, courses):

  with db_cursor() as cur:

    columns = courses.columns.values
    my_tuple = list(courses.itertuples(index=False, name=None))

    insert_query = '''INSERT INTO {} ({})
                      VALUES 
        '''.format(table_name, ', '.join(columns)) + ' %s'

    execute_values(cur, insert_query, my_tuple, template=None, page_size=100)

def get_data(table_name):

  print(table_name)

  with db_cursor() as cur:

    cur.execute('SELECT * FROM %s;' % table_name)
    
    return cur.fetchall()