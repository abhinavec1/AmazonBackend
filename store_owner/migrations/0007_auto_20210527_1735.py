# Generated by Django 3.2.3 on 2021-05-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_owner', '0006_auto_20210527_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopowner',
            name='Latitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=None, max_digits=22),
        ),
        migrations.AlterField(
            model_name='shopowner',
            name='Longitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=None, max_digits=22),
        ),
    ]
