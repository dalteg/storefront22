from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        tables = [
            'store_orderitem', 'store_order', 'store_cartitem',
            'store_cart', 'store_review', 'store_productimage',
            'store_product', 'store_collection'
        ]
        with connection.cursor() as cursor:
            if connection.vendor == 'postgresql':
                cursor.execute('SET session_replication_role = replica;')
                for table in tables:
                    cursor.execute(f'DELETE FROM {table};')
                cursor.execute('SET session_replication_role = DEFAULT;')
                for table, col in [('store_collection', 'id'), ('store_product', 'id')]:
                    cursor.execute(
                        f"SELECT setval(pg_get_serial_sequence('{table}', '{col}'), 1, false);"
                    )
            else:
                cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
                for table in tables:
                    cursor.execute(f'DELETE FROM {table};')
                for table in ['store_collection', 'store_product']:
                    cursor.execute(f'ALTER TABLE {table} AUTO_INCREMENT = 1;')
                cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')

        self.stdout.write('Seeding database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            for statement in sql.split(';'):
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)

        self.stdout.write(self.style.SUCCESS('Done! Database seeded successfully.'))