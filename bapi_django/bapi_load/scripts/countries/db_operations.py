from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              country VARCHAR(250) NOT NULL,
              year INT NOT NULL,
              population INT NOT NULL);
          ''' % table_name)