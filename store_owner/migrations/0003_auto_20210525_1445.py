# Generated by Django 3.2.3 on 2021-05-25 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_owner', '0002_auto_20210525_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='medicine',
            new_name='medName',
        ),
        migrations.RenameField(
            model_name='stocks',
            old_name='quantity',
            new_name='medQnty',
        ),
    ]