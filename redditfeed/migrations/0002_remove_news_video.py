# Generated by Django 3.0 on 2020-09-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redditfeed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='video',
        ),
    ]
