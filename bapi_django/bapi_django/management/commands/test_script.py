from django.core.management.base import BaseCommand
from bapi_django_app.scripts.etl_finance_up import run

class Command(BaseCommand):

    def handle(self, *args, **options):
      run()