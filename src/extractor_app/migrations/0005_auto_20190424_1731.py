# Generated by Django 2.1.8 on 2019-04-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor_app', '0004_auto_20190424_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
