# Generated by Django 2.1.8 on 2019-05-19 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_handler', '0007_auto_20190425_1726'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('username', 'sessionid', 'created')},
        ),
    ]
