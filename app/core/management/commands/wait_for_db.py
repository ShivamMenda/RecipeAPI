"""
Django cmd to wait for db

"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Wait for DB """

    def handle(self, *args, **options):
        """Entrypoint for command"""

        self.stdout.write("Waiting for db...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])  # type: ignore
                db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('db unavailable, waiting 1 second..')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db available!'))
