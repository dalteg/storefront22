from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os
import sys


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Step 1: Clearing existing data...')
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM store_orderitem;')
                cursor.execute('DELETE FROM store_order;')
                cursor.execute('DELETE FROM store_cartitem;')
                cursor.execute('DELETE FROM store_cart;')
                cursor.execute('DELETE FROM store_review;')
                cursor.execute('DELETE FROM store_productimage;')
                cursor.execute('DELETE FROM store_product;')
                cursor.execute('DELETE FROM store_collection;')
                # Reset sequences
                cursor.execute("SELECT setval(pg_get_serial_sequence('store_collection', 'id'), 1, false);")
                cursor.execute("SELECT setval(pg_get_serial_sequence('store_product', 'id'), 1, false);")

            self.stdout.write('Step 2: Reading seed.sql...')
            current_dir = os.path.dirname(__file__)
            file_path = os.path.join(current_dir, 'seed.sql')
            sql = Path(file_path).read_text()

            self.stdout.write('Step 3: Executing seed SQL...')
            with connection.cursor() as cursor:
                cursor.execute(sql)

            self.stdout.write(self.style.SUCCESS('=== SEED COMPLETE ==='))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'SEED FAILED: {str(e)}'))
            import traceback
            self.stdout.write(traceback.format_exc())
            sys.exit(1)