from bapi_django.queries.pools import db_cursor

def create_table(table_name):

  with db_cursor() as cur:
    cur.execute('''CREATE TABLE %s (
              id SERIAL PRIMARY KEY,
              date DATE NOT NULL,
              tag VARCHAR(150) NOT NULL,
              questions INT NOT NULL);
          ''' % table_name)