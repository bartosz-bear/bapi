from bapi_scraping.queries.psycopg2.mydb import db_cursor
from bapi_scraping.queries.psycopg2.courses_queries import delete_table, create_table, insert_values

def inc(x):
  return x + 1

def test_answer():
  assert inc(4) == 5

def test_delete_table():
  with db_cursor() as cur:
    cur.execute('CREATE TABLE test_table;')

    delete_table('test_table')

    a = cur.execute('SELECT * FROM test_table;')
  
    print(a)

  assert a == 'han'





# test in
# test out
