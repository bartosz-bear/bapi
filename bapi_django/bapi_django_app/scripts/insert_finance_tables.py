from bapi_django_app.queries.psycopg2.save_finance import insert_values, insert_values_multi, create_table, delete_table

def insert_tables(checks):
  tables = [{'name': 'clients', 'df': checks['clients']},
        {'name': 'transfers','df': checks['transfers']},
        {'name': 'counties','df': checks['counties']}]

  for t in tables:
    try:
      create_table(t['name'])
      if t['name'] == 'transfers':
        insert_values_multi(t['name'], t['df'])
      else:
        insert_values(t['name'], t['df'])
    except:
      delete_table(t['name'])
      create_table(t['name'])
      if t['name'] == 'transfers':
        insert_values_multi(t['name'], t['df'])
      else:
        insert_values(t['name'], t['df'])