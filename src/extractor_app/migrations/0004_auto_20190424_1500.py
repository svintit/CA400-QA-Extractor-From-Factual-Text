# Generated by Django 2.1.8 on 2019-04-24 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor_app', '0003_auto_20190423_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 24, 15, 0, 36, 610356)),
        ),
    ]
