from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_productimage_image'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DO $$
                BEGIN
                    IF NOT EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name='store_customer' 
                        AND column_name='user_id'
                    ) THEN
                        ALTER TABLE store_customer 
                        ADD COLUMN user_id integer NULL;
                    END IF;
                END $$;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]