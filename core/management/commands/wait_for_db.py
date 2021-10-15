from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for the database...')
        conn = None

        while not conn:
            try:
                conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting for 3 second...')
                time.sleep(3)
        time.sleep(5)
        self.stdout.write(self.style.SUCCESS('Database available!'))
