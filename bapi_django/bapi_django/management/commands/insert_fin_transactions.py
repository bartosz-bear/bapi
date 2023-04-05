from django.core.management.base import BaseCommand
from bapi_transform.scripts.financial_transactions.checks import validate
from bapi_load.scripts.financial_transactions.db_operations import insert_data

class Command(BaseCommand):

    def handle(self, *args, **options):
      insert_data(validate)