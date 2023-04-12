from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              name VARCHAR(250) NOT NULL,
              price NUMERIC(10, 2) NOT NULL,
              product_url TEXT NOT NULL,
              product_image_url TEXT);
          ''' % table_name)