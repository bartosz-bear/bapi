from psycopg2.extras import execute_values
from psycopg2.errors import OperationalError

from bapi_django.queries.pools import db_cursor
from bapi_django.queries.utils import guess_encoding

from sqlalchemy import create_engine
from decouple import config

import psycopg2
import io

import os

def delete_table(table_name):

  with db_cursor() as cur:
    cur.execute('DROP TABLE %s;' % table_name)


def create_table(table_name):

  with db_cursor() as cur:

    file_path = os.getcwd() + '/bapi_load/queries/financial_transactions/create_table_' + table_name + '.sql'

    fd = open(file_path, 'r', encoding=guess_encoding(file_path))
    sqlFile = fd.read()
    fd.close()

    try:
      cur.execute(sqlFile)
    except OperationalError as msg:
      print("Command skipped: ", msg)

def insert_values(table_name, table_data):

  with db_cursor() as cur:
    columns = table_data.columns.values
    my_tuple = list(table_data.itertuples(index=False, name=None))

    insert_query = '''INSERT INTO {} ({})
                      VALUES 
        '''.format(table_name, ', '.join(columns)) + ' %s'

    execute_values(cur, insert_query, my_tuple, template=None, page_size=100)


def insert_values_multi(table_name, table_data):
    
    conn_string = "postgresql+psycopg2://" + config('DB_USER') + ':' + config('DB_PASSWORD') + '@' + config('DB_HOST') + ':' + config('DB_PORT') + '/' + config('DB_NAME')

    engine = create_engine(conn_string)

    table_data.to_sql(table_name, engine, if_exists='replace', index=False)

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    table_data.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    cur.copy_from(output, table_name, null='')
    conn.commit()
    cur.close()
    conn.close()

def execute_many(file_path):

  with db_cursor() as cur:
    # Open and read the file as a single buffer
    
    #file_path = os.getcwd() + '/bapi_django_app/scripts/etl_finance_up.sql'

    fd = open(file_path, 'r', encoding=guess_encoding(file_path))
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')[:3]

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cur.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)