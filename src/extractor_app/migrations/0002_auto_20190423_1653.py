# Generated by Django 2.1.8 on 2019-04-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionid', models.CharField(blank=True, max_length=25, null=True)),
                ('qa_list', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('inputted_text', models.TextField(blank=True, null=True)),
                ('list_title', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='uniquesession',
            unique_together={('sessionid', 'inputted_text', 'list_title', 'qa_list')},
        ),
    ]
