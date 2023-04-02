#!/usr/bin/env python

from psycopg2.extras import execute_values
from psycopg2.errors import OperationalError

from bapi_scraping.queries.psycopg2.mydb import db_cursor
from bapi_scraping.queries.psycopg2.sql_utils import guess_encoding

import os

def run():

  with db_cursor() as cur:
    # Open and read the file as a single buffer
    
    file_path = os.getcwd() + '/bapi_django_app/scripts/etl_finance_up.sql'

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