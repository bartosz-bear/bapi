from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def delete_table(table_name):

  with db_cursor() as cur:
    cur.execute('DROP TABLE %s;' % table_name)


def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              name VARCHAR(250) NOT NULL,
              price NUMERIC(10,2) NOT NULL);
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