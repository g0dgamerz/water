# Generated by Django 2.2.2 on 2019-07-07 05:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
