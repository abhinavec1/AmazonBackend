# Generated by Django 3.2.3 on 2021-05-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='status',
        ),
        migrations.AddField(
            model_name='request',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
