from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

from decouple import config

dbpool = SimpleConnectionPool(1, 20,
  host=config('DB_HOST'),
  port=config('DB_PORT'),
  dbname=config('DB_NAME'),
  user=config('DB_USER'),
  password=config('DB_PASSWORD'),
)

@contextmanager
def db_cursor():
    conn = dbpool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        dbpool.putconn(conn)