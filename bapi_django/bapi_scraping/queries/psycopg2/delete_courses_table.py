import psycopg2
from decouple import config


def delete_courses_table():

  conn = psycopg2.connect("dbname=" + config('DB_NAME') + " user=" + config('DB_USER') + " password=" + config('DB_PASSWORD'))
  cur = conn.cursor()

  cur.execute('DROP TABLE bapi_scraping_courses4;')
  conn.commit()

  cur.close()
  conn.close() 

  return

