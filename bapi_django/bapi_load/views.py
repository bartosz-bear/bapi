from django.shortcuts import render

# Create your views here.
def load_transactions(request):

  return render(request, 'bapi_load/load_transactions.html')