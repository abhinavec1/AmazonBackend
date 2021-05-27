# Generated by Django 3.2.3 on 2021-05-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_owner', '0005_rename_stocks_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopowner',
            name='Latitude',
            field=models.DecimalField(decimal_places=16, default=None, max_digits=22),
        ),
        migrations.AddField(
            model_name='shopowner',
            name='Longitude',
            field=models.DecimalField(decimal_places=16, default=None, max_digits=22),
        ),
    ]