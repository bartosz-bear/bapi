import psycopg2
from decouple import config



def delete_courses_table():

  conn = psycopg2.connect("dbname=" + config('DB_NAME') + " user=" + config('DB_USER') + " password=" + config('DB_PASSWORD'))

  cur = conn.cursor()

  cur.execute('DROP TABLE bapi_scraping_courses4;')

  conn.commit()

  cur.close()

  conn.close() 

  print('well done')

  return

#engine = create_engine("postgresql+psycopg2://" + config("DB_USER") + ":" + config("DB_PASSWORD") + "@localhost:" + config("DB_PORT") + "/" + config("DB_NAME"), echo=True)