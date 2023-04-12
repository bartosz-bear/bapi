from psycopg2.extras import execute_values

from bapi_django.queries.pools import db_cursor

def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              country VARCHAR(250) NOT NULL,
              debt_to_gdp NUMERIC(10,2) NOT NULL);
          ''' % table_name)