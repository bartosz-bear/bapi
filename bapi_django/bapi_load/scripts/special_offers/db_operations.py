from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              name VARCHAR(500) NOT NULL,
              link TEXT NOT NULL,
              special_price NUMERIC(10,2),
              normal_price NUMERIC(10,2) NOT NULL);
          ''' % table_name)