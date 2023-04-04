from django.shortcuts import render

from bapi_transform.scripts.financial_transactions.checks import validate
from bapi_load.scripts.financial_transactions.db_operations import insert_data

def checks(request):

  context = {}

  if request.method == 'POST':

    checks = validate()
    print(checks)
    insert_data(checks)

    context['checks'] = checks['checks_summary']
  else:
    context['transform'] = 'transform'

  return render(request, 'bapi_transform/financial_transactions/transform.html', context)