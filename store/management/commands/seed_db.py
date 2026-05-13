from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        with connection.cursor() as cursor:
            cursor.execute('SET session_replication_role = replica;')
            for table in [
                'store_orderitem', 'store_order', 'store_cartitem',
                'store_cart', 'store_review', 'store_productimage',
                'store_product', 'store_collection'
            ]:
                cursor.execute(f'DELETE FROM {table};')
            cursor.execute('SET session_replication_role = DEFAULT;')
            # Reset sequences
            for table, col in [('store_collection', 'id'), ('store_product', 'id')]:
                cursor.execute(
                    f"SELECT setval(pg_get_serial_sequence('{table}', '{col}'), 1, false);"
                )

        self.stdout.write('Seeding database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)

        self.stdout.write(self.style.SUCCESS('Done! Database seeded successfully.'))