"""
Django command to wait for database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg20pError

from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    # Django command to wait for database to be available

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database to be available....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('Databases are not available, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database ready!'))